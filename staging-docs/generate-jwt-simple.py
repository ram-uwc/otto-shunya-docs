#!/usr/bin/env python3
"""
JWT Token Generator for Otto AI
Uses PyJWT library for proper JWT token generation
"""

import json
import os
import sys
import argparse
from datetime import datetime, timedelta
from typing import Dict, Any
from pathlib import Path

try:
    import jwt
    JWT_AVAILABLE = True
except ImportError:
    JWT_AVAILABLE = False
    print("Warning: PyJWT not available. Install with: pip install PyJWT", file=sys.stderr)


def load_env_file(env_path: str = '.env') -> Dict[str, str]:
    """
    Load environment variables from .env file
    
    Args:
        env_path: Path to .env file
        
    Returns:
        Dictionary of environment variables
    """
    env_vars = {}
    env_file = Path(env_path)
    
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
    
    return env_vars


class JWTGenerator:
    """JWT token generator using PyJWT library"""
    
    def __init__(self, secret_key: str = None, env_file: str = '.env'):
        if not JWT_AVAILABLE:
            raise ImportError("PyJWT library is required. Install with: pip install PyJWT")
        
        # Load .env file if it exists
        env_vars = load_env_file(env_file)
        
        # Priority: explicit secret > .env file > environment variable > default
        self.secret_key = (
            secret_key or 
            env_vars.get('JWT_SECRET_KEY') or 
            os.getenv('JWT_SECRET_KEY') or 
            'default-secret-key'
        )
        self.algorithm = "HS256"
    
    def generate_token(
        self,
        user_id: str,
        company_id: str,
        role: str = "sales_rep",
        expire_hours: int = 24,
        additional_claims: Dict[str, Any] = None
    ) -> str:
        """
        Generate a JWT token using PyJWT
        
        Args:
            user_id: User ID
            company_id: Company ID
            role: User role
            expire_hours: Token expiration in hours
            additional_claims: Additional claims
            
        Returns:
            JWT token string
        """
        now = datetime.utcnow()
        expire = now + timedelta(hours=expire_hours)
        
        # Create payload
        payload = {
            "user_id": user_id,
            "company_id": company_id,
            "role": role,
            "exp": int(expire.timestamp()),
            "iat": int(now.timestamp()),
            "type": "access"
        }
        
        # Add additional claims
        if additional_claims:
            payload.update(additional_claims)
        
        # Generate JWT token using PyJWT
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token
    
    def decode_token(self, token: str) -> Dict[str, Any]:
        """
        Decode token using PyJWT
        
        Args:
            token: JWT token string
            
        Returns:
            Decoded token payload
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
            
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError as e:
            raise ValueError(f"Invalid token: {str(e)}")
    
    def get_token_info(self, token: str) -> Dict[str, Any]:
        """
        Get token information
        
        Args:
            token: JWT-like token string
            
        Returns:
            Token information
        """
        try:
            payload = self.decode_token(token)
            
            return {
                "valid": True,
                "user_id": payload.get('user_id'),
                "company_id": payload.get('company_id'),
                "role": payload.get('role'),
                "issued_at": datetime.fromtimestamp(payload.get('iat', 0)).isoformat(),
                "expires_at": datetime.fromtimestamp(payload.get('exp', 0)).isoformat(),
                "type": payload.get('type')
            }
        except Exception as e:
            return {
                "valid": False,
                "error": str(e)
            }


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Simple JWT Token Generator for Otto AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate token for sales rep (reads JWT_SECRET_KEY from .env file)
  python3 generate-jwt-simple.py -u user-123 -c company-456

  # Generate token for admin
  python3 generate-jwt-simple.py -u admin-123 -c company-456 -r admin

  # Generate token with custom expiration
  python3 generate-jwt-simple.py -u user-123 -c company-456 -e 48

  # Generate token in JSON format
  python3 generate-jwt-simple.py -u user-123 -c company-456 -f json

  # Use custom .env file
  python3 generate-jwt-simple.py -u user-123 -c company-456 --env-file /path/to/.env

  # Override secret from command line
  python3 generate-jwt-simple.py -u user-123 -c company-456 --secret "custom-secret"

  # Debug secret loading
  python3 generate-jwt-simple.py -u user-123 -c company-456 --debug

  # Verify token
  python3 generate-jwt-simple.py --verify "token_here"

  # Get token info
  python3 generate-jwt-simple.py --info "token_here"
        """
    )
    
    parser.add_argument('-u', '--user-id', help='User ID')
    parser.add_argument('-c', '--company-id', help='Company ID')
    parser.add_argument('-r', '--role', default='sales_rep', 
                       choices=['sales_rep', 'customer_rep', 'sales_manager', 'admin'],
                       help='User role (default: sales_rep) - matches schema.md')
    parser.add_argument('-e', '--expire-hours', type=int, default=24,
                       help='Token expiration in hours (default: 24)')
    parser.add_argument('--claims', type=str, help='Additional claims as JSON string')
    parser.add_argument('--secret', help='JWT secret key (overrides .env file and environment)')
    parser.add_argument('--env-file', default='.env', help='Path to .env file (default: .env)')
    parser.add_argument('--verify', help='Verify token validity')
    parser.add_argument('--info', help='Get token information')
    parser.add_argument('-f', '--format', choices=['text', 'json', 'header'], 
                       default='text', help='Output format')
    parser.add_argument('--header-name', default='Authorization',
                       help='Header name for header format')
    parser.add_argument('--debug', action='store_true', help='Show debug information about secret loading')
    
    args = parser.parse_args()
    
    try:
        # Initialize generator
        generator = JWTGenerator(secret_key=args.secret, env_file=args.env_file)
        
        # Debug information
        if args.debug:
            env_file_path = Path(args.env_file)
            print(f"Debug: Looking for .env file at: {env_file_path.absolute()}", file=sys.stderr)
            print(f"Debug: .env file exists: {env_file_path.exists()}", file=sys.stderr)
            
            if env_file_path.exists():
                env_vars = load_env_file(args.env_file)
                has_jwt_secret = 'JWT_SECRET_KEY' in env_vars
                print(f"Debug: JWT_SECRET_KEY found in .env: {has_jwt_secret}", file=sys.stderr)
                if has_jwt_secret:
                    secret_preview = env_vars['JWT_SECRET_KEY'][:10] + "..." if len(env_vars['JWT_SECRET_KEY']) > 10 else env_vars['JWT_SECRET_KEY']
                    print(f"Debug: JWT_SECRET_KEY preview: {secret_preview}", file=sys.stderr)
            
            print(f"Debug: Using secret from: {'command line' if args.secret else '.env file' if Path(args.env_file).exists() and load_env_file(args.env_file).get('JWT_SECRET_KEY') else 'environment variable' if os.getenv('JWT_SECRET_KEY') else 'default'}", file=sys.stderr)
        
        # Handle verification
        if args.verify:
            try:
                generator.decode_token(args.verify)
                is_valid = True
            except ValueError:
                is_valid = False
            
            if args.format == 'json':
                print(json.dumps({"valid": is_valid}))
            else:
                print(f"Token is {'valid' if is_valid else 'invalid'}")
            return
        
        # Handle token info
        if args.info:
            info = generator.get_token_info(args.info)
            if args.format == 'json':
                print(json.dumps(info, indent=2))
            else:
                print("Token Information:")
                for key, value in info.items():
                    print(f"  {key}: {value}")
            return
        
        # Generate token
        if not args.user_id or not args.company_id:
            parser.error("--user-id and --company-id are required for token generation")
        
        # Parse additional claims
        additional_claims = None
        if args.claims:
            try:
                additional_claims = json.loads(args.claims)
            except json.JSONDecodeError as e:
                print(f"Error parsing claims JSON: {e}", file=sys.stderr)
                sys.exit(1)
        
        # Generate token
        token = generator.generate_token(
            user_id=args.user_id,
            company_id=args.company_id,
            role=args.role,
            expire_hours=args.expire_hours,
            additional_claims=additional_claims
        )
        
        # Output token
        if args.format == 'json':
            output = {
                "token": token,
                "user_id": args.user_id,
                "company_id": args.company_id,
                "role": args.role,
                "expire_hours": args.expire_hours,
                "header": f"Bearer {token}"
            }
            print(json.dumps(output, indent=2))
        elif args.format == 'header':
            print(f"{args.header_name}: Bearer {token}")
        else:  # text format
            print("Generated JWT Token:")
            print("=" * 50)
            print(f"Token: {token}")
            print(f"User ID: {args.user_id}")
            print(f"Company ID: {args.company_id}")
            print(f"Role: {args.role}")
            print(f"Expires in: {args.expire_hours} hours")
            print()
            print("Authorization Header:")
            print(f"Authorization: Bearer {token}")
            print()
            print("cURL Example:")
            print(f'curl -H "Authorization: Bearer {token}" http://localhost:8000/api/v1/storage/list')
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
