# Boxx Insurance - WhatsApp Static Exploratory Journey

## Overview
This document defines the WhatsApp chatbot experience for Boxx Insurance customers. Unlike the voice agent (which is conversational and free-flowing), the WhatsApp journey is **structured and menu-driven**, allowing users to explore options through buttons, quick replies, and lists.

**Version:** 1.0  
**Last Updated:** November 2025  
**Platform:** WhatsApp Business API  
**Channel Type:** Static/Structured with Exploratory Navigation

---

## Table of Contents
1. [Journey Design Principles](#journey-design-principles)
2. [Entry Points & Welcome Flow](#entry-points--welcome-flow)
3. [Main Menu Structure](#main-menu-structure)
4. [Incident Reporting Flow](#incident-reporting-flow)
5. [Education & Resources Flow](#education--resources-flow)
6. [Insurance Information Flow](#insurance-information-flow)
7. [Support & Help Flow](#support--help-flow)
8. [Message Templates](#message-templates)
9. [WhatsApp Features Used](#whatsapp-features-used)
10. [Technical Integration](#technical-integration)

---

## 1. Journey Design Principles

### Core Principles

**📱 Mobile-First**
- Short messages (1-3 sentences max)
- Clear button labels (max 20 characters)
- Visual hierarchy with emojis
- Quick to complete (< 5 minutes per task)

**🔄 Non-Linear Navigation**
- Users can explore different paths
- Easy to go back to main menu
- Breadcrumb context (where am I?)
- "Start Over" always available

**🎯 Goal-Oriented**
- Each flow has clear outcome
- Progress indicators for multi-step flows
- Confirmation at end of each journey
- Next action suggestions

**💬 Conversational Yet Structured**
- Friendly, empathetic tone
- Use customer's name when available
- Acknowledge their situation
- Provide clear options, not open text input

**🔗 Integration with Voice & Web**
- Can escalate to voice call
- Links to web app for complex tasks
- Consistent information across channels
- Unified incident IDs

---

## 2. Entry Points & Welcome Flow

### Entry Point 1: User Initiates Chat

**Trigger:** User sends any message to Boxx WhatsApp number

**Flow:**
```
Bot: Hi there! 👋

Welcome to Boxx Insurance. I'm here to help you with cyber incidents 
and protection.

What brings you here today?

[Button: 🚨 Report Cyber Incident]
[Button: 📚 Learn About Cyber Safety]
[Button: 📋 My Insurance Info]
[Button: 💬 Talk to Support]
```

### Entry Point 2: QR Code Scan (from Policy Document)

**Trigger:** User scans QR code from insurance policy

**Flow:**
```
Bot: Hi [Name]! 👋

I recognize you from your policy. Welcome back!

Your Boxx Protection Plan: Active ✅
Coverage: ₹[Amount]

How can I help you today?

[Button: 🚨 Report Incident]
[Button: 📊 View My Coverage]
[Button: 📚 Safety Resources]
[Button: 👤 Account Settings]
```

### Entry Point 3: Post-Call Follow-up

**Trigger:** Automated message after voice call with agent

**Flow:**
```
Bot: Hi [Name],

Following up on your call about [Incident Type].

Your Incident ID: C-[number]

Would you like to:

[Button: 📄 View Incident Details]
[Button: 📎 Upload Evidence]
[Button: 📞 Call Back]
[Button: ✅ I'm All Set]
```

### Entry Point 4: Marketing/Outreach Campaign

**Trigger:** User clicks WhatsApp link from email/SMS campaign

**Flow:**
```
Bot: Hi! 👋

Thanks for your interest in Boxx Cyber Insurance!

Did you know? 1 in 3 people in India experience cyber fraud. 
We protect you from:

• UPI & Card Fraud 💳
• Identity Theft 🆔
• Ransomware 🔒
• Social Media Hacks 📱
• And more...

[Button: 🛡️ Get Protected]
[Button: 📖 Learn More]
[Button: 💬 Talk to Expert]
```

### Entry Point 5: Returning User

**Trigger:** User who has interacted before returns

**Flow:**
```
Bot: Welcome back, [Name]! 👋

Last time, you were [context: checking coverage/learning about scams].

Pick up where you left off:

[Button: 🚨 Report New Incident]
[Button: 📊 My Dashboard]
[Button: 📚 Continue Learning]
[Button: 🔍 Main Menu]
```

---

## 3. Main Menu Structure

### Main Menu (Hub)

```
🏠 MAIN MENU

[Button: 🚨 Report Cyber Incident]
[Button: 📚 Learn & Protect]
[Button: 📋 My Insurance]
[Button: 💬 Get Help]
[Button: ⚙️ Settings]

Type "menu" anytime to return here.
```

### Quick Actions (Always Available)

**Throughout the journey, users can type:**
- `menu` → Return to main menu
- `help` → Get contextual help
- `agent` → Talk to human agent
- `call` → Request callback
- `status` → Check incident status (if any open incidents)

---

## 4. Incident Reporting Flow

### 4.1 Incident Type Selection

**User clicks:** [🚨 Report Cyber Incident]

**Bot Response:**
```
🚨 REPORT CYBER INCIDENT

I'm here to help. First, what happened?

Select the situation closest to yours:

[List Item 1: 💸 Someone Got My Money]
[List Item 2: 🔐 My Account Was Hacked]
[List Item 3: 📱 Suspicious Call/Message]
[List Item 4: 💻 Computer Problem]
[List Item 5: 🆔 Identity Misuse]
[List Item 6: 🤔 I'm Not Sure]

[Button: ⬅️ Back to Menu]
```

### 4.2 Sub-Category Selection

**User selects:** [💸 Someone Got My Money]

**Bot Response:**
```
💸 MONEY LOST

Which of these happened?

[Button: 📲 I gave away my OTP]
[Button: 💳 Card details were used]
[Button: 🏦 Unauthorized bank transfer]
[Button: 🛒 Fake online shopping]
[Button: 📦 Fake delivery payment]
[Button: 🔙 Go Back]
```

**User selects:** [🔐 My Account Was Hacked]

**Bot Response:**
```
🔐 ACCOUNT HACKED

Which account?

[Button: 📧 Email]
[Button: 📱 WhatsApp/Social Media]
[Button: 🏦 Banking/UPI App]
[Button: 🔙 Go Back]
```

**User selects:** [📱 Suspicious Call/Message]

**Bot Response:**
```
📱 SUSPICIOUS CONTACT

What did they claim to be?

[Button: 🏦 Bank/Finance Company]
[Button: 📦 Courier/Delivery]
[Button: 👮 Police/Government]
[Button: 🎁 Lottery/Prize]
[Button: 🔙 Go Back]
```

**User selects:** [💻 Computer Problem]

**Bot Response:**
```
💻 COMPUTER ISSUE

What's happening?

[Button: 🔒 Locked/Ransom Message]
[Button: 🐛 Virus Warning Popup]
[Button: 🐌 Running Very Slow]
[Button: 📁 Files Missing/Changed]
[Button: 🔙 Go Back]
```

**User selects:** [🆔 Identity Misuse]

**Bot Response:**
```
🆔 IDENTITY MISUSE

What did you discover?

[Button: 💳 Unknown Loan/Credit Card]
[Button: 📱 Unknown Mobile Connection]
[Button: 🏦 Unknown Bank Account]
[Button: 🆔 Aadhaar/PAN Misuse]
[Button: 🔙 Go Back]
```

**User selects:** [🤔 I'm Not Sure]

**Bot Response:**
```
🤔 LET'S FIGURE IT OUT

Answer a few quick questions:

❓ Did you lose money?

[Button: Yes, money is gone]
[Button: No money lost yet]
[Button: Not sure]
```

### 4.3 Quick Triage Questions

**Based on incident type, ask 3-4 key questions using quick replies:**

**Example: User selected "I gave away my OTP"**

```
Bot: When did this happen?

[Quick Reply: Just now (< 1 hour)]
[Quick Reply: Today]
[Quick Reply: Yesterday]
[Quick Reply: More than 2 days ago]

---

Bot: How much money was taken?

[Quick Reply: Less than ₹5,000]
[Quick Reply: ₹5,000 - ₹25,000]
[Quick Reply: ₹25,000 - ₹1,00,000]
[Quick Reply: More than ₹1,00,000]

---

Bot: Do you still have access to your UPI/banking app?

[Quick Reply: Yes]
[Quick Reply: No, can't login]
[Quick Reply: Not sure]
```

### 4.4 Immediate Safety Guidance

**Bot analyzes responses and provides immediate action:**

**If CRITICAL (active threat, recent, money at risk):**

```
🚨 URGENT ACTION NEEDED

Based on what you shared, we need to secure your account RIGHT NOW.

I'll guide you step by step. Ready?

[Button: ✅ Yes, Let's Start]
[Button: 📞 Call Me Instead]

[Status bar: Step 1 of 5]
```

**If MEDIUM (past incident, contained):**

```
✅ Situation Assessment

The immediate threat has passed. Let me help you:
1. Document everything properly
2. Check your coverage
3. File necessary reports

[Button: 📝 Continue with Report]
[Button: 📞 Talk to Agent]
```

### 4.5 Step-by-Step Safety Instructions

**Bot provides one instruction at a time:**

```
🔒 STEP 1 of 5

Open your [UPI App Name] right now.

Done?

[Button: ✅ Done, Next Step]
[Button: ❌ Can't Find It]
[Button: 📞 Need Help]

---

🔒 STEP 2 of 5

Look for 'Block UPI' or 'Freeze Payments'.

Found it?

[Button: ✅ Yes, Found It]
[Button: ❌ Don't See This Option]
[Button: 📷 Send Screenshot]

---

🔒 STEP 3 of 5

Tap on 'Block UPI ID' now.

[Button: ✅ Done]
[Button: ⚠️ It's Not Working]

---

✅ ACCOUNT SECURED!

Great job! Your account is now protected.

Next steps:
1. Document the incident ✅
2. Check coverage ✅
3. File reports ✅

[Button: 📝 Continue]
```

### 4.6 Evidence Collection

```
📎 EVIDENCE UPLOAD

To process your claim, I need some evidence.

Please upload:
✅ Screenshots of scam messages
✅ Transaction receipts
✅ Any other proof you have

[Button: 📷 Take Photo]
[Button: 📁 Upload from Gallery]
[Button: ⏭️ Skip for Now]
[Button: 💬 I Don't Have Any]

---

[After each upload]

Bot: ✅ Received [Image name]

Upload more?

[Button: 📷 Upload Another]
[Button: ✅ That's All]
```

### 4.7 Incident Summary & Confirmation

```
📋 INCIDENT SUMMARY

Review your report:

📌 Type: UPI OTP Scam
🕐 When: Today, [time]
💰 Amount: ₹[amount]
🏦 Bank/App: [name]
📎 Evidence: 3 files attached
🔒 Safety: Account secured ✅

Everything correct?

[Button: ✅ Submit Report]
[Button: ✏️ Edit Details]
[Button: ❌ Cancel]

---

[After submit]

✅ REPORT SUBMITTED

Incident ID: C-48271

📧 Confirmation sent to your email
📱 SMS sent with details

What happens next:
1. Claims team reviews (within 24 hrs)
2. They may contact you for more info
3. You'll get updates via WhatsApp

[Button: 📊 View Coverage]
[Button: 📞 Talk to Claims Team]
[Button: 🏠 Main Menu]
```

### 4.8 Coverage Check

```
🛡️ YOUR COVERAGE

Good news! This incident is COVERED ✅

Your Plan: Individual Protection
Max Coverage: ₹1,00,000
This Incident: ₹[amount] claimed

📋 What's covered:
• Financial loss up to limit
• Professional recovery assistance
• Legal support if needed
• 3-year credit monitoring (for identity theft)

⏱️ Claim Timeline:
• Review: 24-48 hours
• Decision: 7-10 days
• Payout: 3-5 days after approval

[Button: 📄 View Full Policy]
[Button: 💬 Ask Claims Question]
[Button: ✅ Got It]
```

### 4.9 Wellness Check & Stella Handoff

```
🧘 HOW ARE YOU FEELING?

Cyber incidents can be stressful. It's normal to feel:
• Anxious 😰
• Angry 😤
• Embarrassed 😳
• Worried 😟

Our wellness assistant Stella can help you process these feelings.

[Button: 💚 Talk to Stella]
[Button: 📚 Read Self-Help Tips]
[Button: ✅ I'm Okay]

---

[If user clicks Talk to Stella]

Bot: Great! Connecting you with Stella...

[Switch to Stella bot context]

Stella: Hi [Name], I'm Stella. I'm here to support you through this. 
What you experienced wasn't your fault, and your feelings are completely 
valid. 

How are you feeling right now?

[Button: Stressed/Anxious]
[Button: Angry/Frustrated]
[Button: Embarrassed/Ashamed]
[Button: Just Want to Move On]
```

### 4.10 Follow-up Actions

```
📋 NEXT STEPS

Here's what you should do:

☐ File Police Complaint
   (Required for claims > ₹25,000)
   [Button: 📍 Find Nearest Cyber Cell]

☐ Report on Cybercrime Portal
   cybercrime.gov.in
   [Button: 🔗 Open Link]

☐ Block Scammer Number
   [Button: 📱 Report on Sanchar Saathi]

☐ Change Passwords
   [Button: 📝 See Checklist]

☐ Download Boxx App
   Track your claim & get safety tips
   [Button: 📲 Download App]

[Button: ✅ Done with Everything]
[Button: 💬 I Have Questions]
```

---

## 5. Education & Resources Flow

### 5.1 Learn & Protect Menu

**User clicks:** [📚 Learn & Protect]

```
📚 LEARN & PROTECT

Stay safe online with our resources:

[Button: 🎓 Cyber Safety Courses]
[Button: 🎬 Video Tutorials]
[Button: 📊 Take Risk Assessment]
[Button: 🚨 Latest Scam Alerts]
[Button: 📖 Safety Guides]
[Button: 🎮 Interactive Quiz]

[Button: ⬅️ Back to Menu]
```

### 5.2 Cyber Safety Courses

```
🎓 CYBER SAFETY COURSES

Choose a topic:

[List: 🔐 Password Security 101] (5 min)
[List: 📱 OTP & UPI Safety] (3 min)
[List: 📧 Spotting Phishing Emails] (7 min)
[List: 🛒 Safe Online Shopping] (6 min)
[List: 💬 Social Media Security] (5 min)
[List: 🏦 Recognizing Fake Bank Calls] (8 min)

[Button: 🏆 My Progress]
[Button: ⬅️ Back]

---

[When user selects a course]

🔐 PASSWORD SECURITY 101

📚 5-minute interactive lesson

You'll learn:
✓ How to create strong passwords
✓ Why you need unique passwords
✓ Using password managers
✓ Two-factor authentication

Ready to start?

[Button: ▶️ Start Lesson]
[Button: 📱 Save for Later]

---

[Lesson format - Interactive cards]

Bot: 📖 LESSON 1/5

❌ BAD PASSWORD:
"password123"
"JohnDoe2024"
"12345678"

Why? Easy to guess, common patterns.

✅ GOOD PASSWORD:
"Tr0pic@l$unset!92"
"C0ff33&D0nuts#47"

Why? Mix of uppercase, lowercase, numbers, symbols.

[Button: ▶️ Next]
[Button: ℹ️ Tell Me More]

---

Bot: 📝 QUICK CHECK

Which password is stronger?

A) Mumbai2024
B) M$k7pQw!9zF3
C) ilovemydog

[Button: A]
[Button: B]
[Button: C]

---

[After correct answer]

Bot: ✅ Correct! B is much stronger.

Why? It has:
• Mixed case letters
• Numbers
• Special symbols  
• No dictionary words
• Hard to guess

[Button: ▶️ Continue]

---

[End of course]

Bot: 🎉 COURSE COMPLETE!

You've learned:
✅ Strong password creation
✅ Password manager basics
✅ Two-factor authentication
✅ Common mistakes to avoid

📊 Your Score: 9/10

[Button: 📜 Get Certificate]
[Button: 🎓 Take Another Course]
[Button: 📱 Share Achievement]
```

### 5.3 Video Tutorials

```
🎬 VIDEO TUTORIALS

Short, practical videos:

[Media Card: OTP Safety Video]
🎬 Never Share Your OTP
⏱️ 2:17 mins • 45K views
[Button: ▶️ Watch]

[Media Card: Marketplace Safety]
🎬 Safe Buying on OLX & Facebook
⏱️ 3:42 mins • 32K views
[Button: ▶️ Watch]

[Media Card: Recognizing Fake Calls]
🎬 Spot Fake Bank Calls
⏱️ 4:15 mins • 58K views
[Button: ▶️ Watch]

[Media Card: Parcel Scam Alert]
🎬 Fake Delivery Messages
⏱️ 2:58 mins • 41K views
[Button: ▶️ Watch]

[Button: 📱 More Videos]
[Button: ⬅️ Back]

---

[When watching video]

[Video player with controls]

🎬 Never Share Your OTP
⏱️ 2:17

[Progress bar]

[Button: ⏸️ Pause]
[Button: 💾 Save to Watch Later]
[Button: 📤 Share with Friend]

---

[After video]

Bot: Did you find this helpful?

[Button: 👍 Very Helpful]
[Button: 😐 Somewhat Helpful]
[Button: 👎 Not Helpful]

Would you like to:

[Button: 🎬 Watch Related Video]
[Button: 📖 Read Full Guide]
[Button: 📱 Get Reminder to Practice]
```

### 5.4 Risk Assessment

```
📊 CYBER SAFETY RISK ASSESSMENT

Find out how safe you are online!

⏱️ Takes: 5 minutes
❓ Questions: 15
📈 You'll get: Personalized safety score & tips

[Button: ▶️ Start Assessment]
[Button: ℹ️ What's This About?]
[Button: ⬅️ Back]

---

[Assessment questions - one at a time]

Bot: 📊 QUESTION 1/15

Do you use the same password for multiple accounts?

[Button: Yes, same password]
[Button: I have 2-3 passwords]
[Button: Unique password for each]
[Button: I use a password manager]

---

Bot: 📊 QUESTION 2/15

Do you have two-factor authentication on your banking apps?

[Button: Yes, all banking apps]
[Button: On some apps]
[Button: No]
[Button: I don't know what that is]

---

[Continue through all 15 questions]

---

[Results]

Bot: 📊 YOUR CYBER SAFETY SCORE

🎯 Score: 6.5/10

Status: Medium Risk ⚠️

You have solid security habits, but there are key areas to improve.

📉 Your Weakest Areas:
1. Two-Factor Authentication
2. Password Strength
3. Social Media Security

📈 Your Strongest Areas:
1. Banking Awareness
2. Device Security

[Button: 📋 See Full Report]
[Button: 💡 Get Improvement Plan]
[Button: 📤 Share Result]

---

[Improvement plan]

Bot: 💡 YOUR PERSONALIZED PLAN

🎯 PRIORITY 1: Enable Two-Factor Auth
Why: Stops 90% of account hacks
Time: 10 minutes

[Button: 📖 How to Enable 2FA]
[Button: ✅ Done, Next Priority]

🎯 PRIORITY 2: Strengthen Passwords
Why: Weak passwords = easy target
Time: 15 minutes

[Button: 📖 Password Guide]
[Button: ✅ Done, Next Priority]

🎯 PRIORITY 3: Secure Social Media
Why: Often the first entry point
Time: 20 minutes

[Button: 📖 Social Media Guide]
[Button: ✅ Done, Next Priority]

[Button: 📅 Remind Me in 1 Week]
[Button: 🏠 Main Menu]
```

### 5.5 Latest Scam Alerts

```
🚨 LATEST SCAM ALERTS

Stay updated on current threats:

⚠️ TRENDING NOW:

[Alert Card]
🚨 Fake UPI Refund Calls
⏰ Last 7 days • 2,341 reports
Don't share OTP for "refunds"!
[Button: 📖 Read More]

[Alert Card]
📦 Fake Parcel Customs Fee
⏰ This week • 1,876 reports
No legit courier asks for customs via SMS
[Button: 📖 Read More]

[Alert Card]  
💳 QR Code Payment Scam
⏰ New threat • 892 reports
Scan only from trusted sources
[Button: 📖 Read More]

[Button: 🔔 Turn On Alerts]
[Button: 📍 Scams in My Area]
[Button: ⬅️ Back]

---

[When user reads more]

🚨 FAKE UPI REFUND CALLS

What's happening:
• You get a call from "UPI support"
• They say you'll get a refund
• They ask for OTP to "process refund"
• Money gets stolen instead

🚩 Red Flags:
• Calls about refunds you didn't request
• Urgency: "Expires today!"
• Asking for OTP over phone
• Unknown number

✅ What to Do:
1. Hang up immediately
2. Don't share OTP/PIN
3. No legitimate refund needs OTP
4. Report: Type "scam" below

[Button: 🚨 I Got This Call!]
[Button: 🔗 Share Warning]
[Button: ✅ Thanks, Got It]
```

### 5.6 Interactive Quiz

```
🎮 CYBER SAFETY QUIZ

Test your knowledge! Can you spot the scams?

🏆 High Score: 850 points
👥 24,532 people played today

[Button: 🎮 Play Now]
[Button: 🏆 View Leaderboard]
[Button: ⬅️ Back]

---

[Quiz gameplay]

Bot: 🎮 ROUND 1/10

You receive this SMS:

"Dear customer, your parcel could not 
be delivered. Pay ₹89 customs fee to 
receive: bit.ly/xyz123"

Is this a scam?

⏱️ 10 seconds

[Button: ✅ Yes, Scam]
[Button: ❌ No, Legitimate]

---

[If correct]

Bot: ✅ CORRECT! +100 points

🎯 Score: 100

Why it's a scam:
• Short URL (bit.ly) - suspicious
• Real couriers don't SMS about customs
• Payment before delivery is a red flag

[Button: ▶️ Next Question]

---

[End of quiz]

Bot: 🎉 QUIZ COMPLETE!

🎯 Your Score: 850/1000

🏅 Rank: Top 15% today!
📊 Accuracy: 85%

What you're great at:
✅ Spotting fake messages
✅ Recognizing phishing

Work on:
⚠️ Social engineering tactics

[Button: 🎮 Play Again]
[Button: 📤 Share Score]
[Button: 🏆 View Leaderboard]
```

---

## 6. Insurance Information Flow

### 6.1 My Insurance Menu

**User clicks:** [📋 My Insurance]

```
📋 MY INSURANCE

[If logged in]

Hi [Name]! 👋

Plan: Individual Protection Plan
Status: Active ✅
Valid Until: [Date]

[Button: 📊 View Coverage Details]
[Button: 📄 Policy Document]
[Button: 💰 Make Payment]
[Button: 📞 Upgrade Plan]
[Button: 🎁 Refer & Earn]

[Button: ⬅️ Back to Menu]

---

[If not logged in]

Please verify your identity first:

[Button: 📱 Login with Mobile]
[Button: 📧 Login with Email]
[Button: 🆕 New Customer]
```

### 6.2 Coverage Details

```
📊 YOUR COVERAGE

Individual Protection Plan
₹2,999/year

What's Covered:

💰 UPI/OTP Fraud
Coverage: ₹1,00,000
Status: Available ✅

💳 Card Fraud
Coverage: ₹2,00,000
Status: Available ✅

🔒 Ransomware
Coverage: ₹3,00,000
Status: Available ✅

🆔 Identity Theft
Coverage: ₹5,00,000
Status: Available ✅

[Button: 📋 See All Coverage]
[Button: ❓ What's Not Covered?]
[Button: 📞 Upgrade Coverage]

---

[See All Coverage]

Bot: 📋 COMPLETE COVERAGE LIST

✅ UPI/OTP Scam → ₹1,00,000
✅ Card Fraud → ₹2,00,000
✅ Net Banking Fraud → ₹2,00,000
✅ E-commerce Scam → ₹50,000
✅ Email Hack → ₹25,000
✅ Social Media Hack → ₹25,000
✅ Vishing/Fake Calls → ₹1,50,000
✅ Ransomware → ₹3,00,000
✅ Identity Theft → ₹5,00,000
✅ Marketplace Fraud → ₹30,000
✅ Parcel Scam → ₹75,000

Annual Limit: ₹2,00,000

[Button: 📄 Download Full Policy]
[Button: 💬 Ask Question]
```

### 6.3 Active Claims

```
📂 MY CLAIMS

You have 1 active claim:

[Claim Card]
🔴 Incident: UPI OTP Scam
📅 Filed: Nov 15, 2025
💰 Amount: ₹45,000
📊 Status: Under Review

Last Update: Nov 17, 2025
"Claims team reviewing evidence"

[Button: 👁️ View Details]
[Button: 📎 Upload More Evidence]
[Button: 📞 Call Claims Team]

---

[View claim details]

Bot: 📂 CLAIM DETAILS

Incident ID: C-48271
Type: UPI OTP Scam
Date: Nov 15, 2025
Amount: ₹45,000

Timeline:
✅ Nov 15: Report submitted
✅ Nov 16: Initial review complete
🔄 Nov 17: Evidence verification
⏳ Pending: Bank coordination
⏳ Pending: Final decision

Estimated Decision: Nov 22, 2025

Documents Uploaded:
✅ Transaction screenshots (3)
✅ SMS proof (1)
✅ Police complaint (1)

[Button: 📎 Add More Documents]
[Button: 💬 Ask About Status]
[Button: 📧 Email Updates]
```

### 6.4 Policy Document

```
📄 POLICY DOCUMENT

Your policy is ready:

[Document Preview]
📄 Boxx Insurance Policy
Individual Protection Plan
Policy #: BX-2024-[number]
Valid: [Date] to [Date]

[Button: 📲 Download PDF]
[Button: 📧 Email to Me]
[Button: 📤 Share]
[Button: 👁️ View in Browser]

Also available:
• Policy Schedule
• Terms & Conditions
• Claim Form
• Renewal Certificate

[Button: 📂 Download All]
```

### 6.5 Upgrade Plan

```
📞 UPGRADE YOUR PLAN

Compare plans:

[Plan Card: Current]
Individual Plan
₹2,999/year
Coverage: ₹1L - ₹5L per incident

[Plan Card: Upgrade Option 1]
Family Plan (4 members)
₹4,999/year (+₹2,000)
Coverage: 1.5x - 2x higher
SAVE: ₹3,998/year vs individual plans

[Button: ℹ️ Compare Details]
[Button: ✅ Upgrade to Family]

[Plan Card: Upgrade Option 2]
SMB Plan
From ₹15,000/year
Coverage: 5x - 10x higher
Includes: Business coverage, employee protection

[Button: ℹ️ Learn More]
[Button: 📞 Talk to Business Expert]

[Button: ⬅️ Maybe Later]
```

---

## 7. Support & Help Flow

### 7.1 Get Help Menu

**User clicks:** [💬 Get Help]

```
💬 GET HELP & SUPPORT

How can we help you?

[Button: 📞 Call Support]
[Button: 💬 Chat with Agent]
[Button: ❓ FAQs]
[Button: 📧 Email Us]
[Button: 💬 Stella (Wellness Support)]

[Button: ⬅️ Back to Menu]
```

### 7.2 Call Support

```
📞 CALL SUPPORT

We're here 24x7 to help!

[Button: 📞 Call Now] 
(Tap to call: 1800-XXX-XXXX)

Or request a callback:

[Button: 📞 Call Me in 2 Minutes]
[Button: 📞 Schedule Callback]

Business Hours: 24x7
Average Wait: < 2 mins

Language Support:
🇮🇳 Hindi & English
```

### 7.3 Chat with Agent

```
💬 CHAT WITH AGENT

Connecting you to our support team...

⏱️ Average wait time: 3 minutes

While you wait, tell me briefly what you need help with:

[Quick Reply: Claim Status]
[Quick Reply: Policy Question]
[Quick Reply: Technical Issue]
[Quick Reply: Other]

---

[Once connected]

Bot: ✅ Connected to Agent Priya

Agent Priya: Hi [Name]! 👋 I'm Priya from Boxx Support. I can see you need help with [topic]. How can I assist you?

[Regular chat conversation]

---

[When agent closes]

Agent Priya: Is there anything else I can help you with today?

[Button: ✅ I'm All Set]
[Button: 🆕 New Question]

---

Bot: Thanks for chatting with us!

How was your experience with Agent Priya?

[Button: 😊 Excellent]
[Button: 🙂 Good]
[Button: 😐 Okay]
[Button: 😞 Poor]

[After rating]

Bot: Thank you for your feedback!

[Button: 🏠 Main Menu]
```

### 7.4 FAQs

```
❓ FREQUENTLY ASKED QUESTIONS

Choose a category:

[List: 💳 Claims & Coverage]
[List: 💰 Payments & Billing]
[List: 📱 Account & Login]
[List: 🚨 Reporting Incidents]
[List: 📖 Policy & Terms]
[List: 🔒 Security & Privacy]

[Button: 🔍 Search FAQs]
[Button: ⬅️ Back]

---

[Claims & Coverage FAQs]

❓ CLAIMS & COVERAGE

[Expandable Item: How long does claim processing take?]
[Expandable Item: What documents do I need?]
[Expandable Item: How do I check claim status?]
[Expandable Item: What if my claim is denied?]
[Expandable Item: Can I file a claim online?]

[Button: 💬 Still Have Questions?]

---

[When user clicks an item]

Bot: ❓ How long does claim processing take?

✅ Standard Timeline:
• Initial review: 24-48 hours
• Documentation check: 2-3 days
• Bank coordination: 5-7 days  
• Final decision: 7-10 days
• Payout: 3-5 days after approval

🚨 Priority Cases (ransomware, high-value):
• Faster processing
• Dedicated case manager
• Real-time updates

[Button: 📊 Track My Claim]
[Button: ❓ Another Question]
```

---

## 8. Message Templates

### 8.1 Daily Check-in (Proactive Engagement)

**Trigger:** User has open incident, sent at 10 AM daily

```
🌅 Good morning, [Name]!

Quick update on your incident (C-[number]):

📊 Status: [Current status]
⏭️ Next Step: [What's happening next]
⏰ ETA: [Expected timeline]

Everything okay? Need anything?

[Button: 👍 All Good]
[Button: ❓ I Have a Question]
[Button: 📞 Call Me]

Type "stop updates" to pause daily check-ins.
```

### 8.2 Scam Alert (Proactive Warning)

**Trigger:** New trending scam in user's area

```
🚨 SCAM ALERT IN YOUR AREA

⚠️ Fake [Bank Name] Calls Reported
📍 [City] • Last 24 hours • 47 reports

What they do:
They call claiming to be from [bank], asking for OTP to "secure" your account.

🚩 Remember:
❌ Banks NEVER ask for OTP
❌ Don't share OTP with anyone
✅ Hang up and call bank directly

[Button: 📖 Read More]
[Button: ✅ Thanks for Warning]
[Button: 🚨 I Got This Call!]

Stay safe! 🛡️
```

### 8.3 Educational Reminder

**Trigger:** User hasn't engaged with education content in 30 days

```
💡 QUICK CYBER SAFETY TIP

Did you know?

Using the same password across multiple accounts is like using one key for your house, car, and office! 🔑

If one gets stolen, everything is at risk.

[Button: 🎓 Learn Password Safety]
[Button: 📊 Take Risk Assessment]
[Button: ⏭️ Maybe Later]

New tip every week! 💡
```

### 8.4 Payment Reminder

**Trigger:** Policy renewal due in 15 days

```
⏰ RENEWAL REMINDER

Hi [Name]!

Your Boxx Protection Plan expires in 15 days.

Current Plan: Individual
Annual Premium: ₹2,999

Renew now to continue protection:

[Button: 💳 Pay Now]
[Button: 📞 Upgrade Plan]
[Button: 💬 Talk to Us]

Don't let your protection lapse! 🛡️
```

### 8.5 Claim Decision

**Trigger:** Claim approved or denied

**Approved:**
```
✅ CLAIM APPROVED!

Great news, [Name]!

Your claim (C-[number]) has been approved.

💰 Approved Amount: ₹[amount]
📅 Payout Date: [date]
🏦 Account: [masked account number]

Money will be credited within 3-5 business days.

[Button: 📄 View Decision Letter]
[Button: 🏦 Update Bank Details]
[Button: 💬 Ask Question]

Thank you for choosing Boxx! 🛡️
```

**Denied:**
```
📋 CLAIM DECISION

Hi [Name],

After careful review, we're unable to approve your claim (C-[number]).

Reason: [Brief reason]

💬 We understand this is disappointing. Let us explain:

[Button: 📄 View Detailed Explanation]
[Button: ↩️ Appeal Decision]
[Button: 📞 Talk to Claims Manager]

You have 30 days to appeal.
```

### 8.6 Wellness Check-in

**Trigger:** 3 days after high-stress incident reported

```
🧘 HOW ARE YOU DOING?

Hi [Name],

It's been a few days since the incident. 

Experiencing cyber fraud can be stressful. It's normal to feel:
• Anxious 😰
• Angry 😤
• Embarrassed 😳

How are you feeling now?

[Button: 😊 Much Better]
[Button: 😐 Still Processing]
[Button: 😟 Still Stressed]
[Button: 💬 Talk to Stella]

Remember: You did nothing wrong. 💚
```

---

## 9. WhatsApp Features Used

### 9.1 Interactive Messages

**Quick Reply Buttons**
- Max 3 buttons per message
- Used for binary choices, simple selections
- Example: Yes/No, Done/Need Help

**List Messages**
- Up to 10 items per list
- Used for categorical choices
- Example: Incident type selection, FAQ categories

**Call-to-Action Buttons**
- Phone number buttons (initiate call)
- URL buttons (open links)
- Example: Call support, Open policy document

### 9.2 Rich Media

**Images**
- Infographics (safety tips)
- Screenshots (how-to guides)
- Charts (coverage comparison)

**Videos**
- Short educational content (< 5 min)
- Step-by-step tutorials
- Scam awareness videos

**Documents**
- Policy PDFs
- Claim forms
- Certificates
- Evidence uploads

**Location**
- Nearest police cyber cell
- Branch locations
- Verified service centers

### 9.3 Message Types

**Template Messages** (24h+ window)
- Transactional updates
- Policy reminders
- Claim status updates
- Scam alerts

**Session Messages** (< 24h window)
- Interactive conversation
- Real-time responses
- Evidence collection

**Quick Replies**
- Pre-defined response options
- Faster than typing
- Analytics on user choices

### 9.4 WhatsApp Business Features

**Business Profile**
- Company name: Boxx Insurance
- Description: Cyber Insurance & Protection
- Hours: 24x7 Support Available
- Website link
- Email address

**Catalog** (Optional)
- Different insurance plans
- Add-on coverages
- Educational resources

**Away Message**
- "Thanks for messaging! We typically reply within 2 minutes."

**Greeting Message**
- Shown on first contact (Entry Point 1)

**Labels** (Internal)
- New Lead
- Active Customer
- Open Incident
- Hot Lead
- VIP Customer

---

## 10. Technical Integration

### 10.1 Architecture

```
User's WhatsApp
    ↓
WhatsApp Business API
    ↓
Webhook Handler (Backend)
    ↓
Intent Classification (NLU/NLP)
    ↓
Dialog Manager
    ↓
Knowledge Base (RAG)
    ↓
Response Generator
    ↓
WhatsApp Business API
    ↓
User's WhatsApp
```

### 10.2 Integration Points

**User Authentication**
- OTP verification via SMS
- Link to policy number
- Session management

**Knowledge Base Access**
- Query boxx_incident_types.md for classification
- Query boxx_safety_procedures.md for step-by-step guidance
- Query boxx_coverage_policies.md for coverage info
- Query boxx_educational_resources.md for content
- Query boxx_support_resources.md for platform help

**Incident Management System**
- Create incident records
- Update incident status
- Link evidence uploads
- Generate incident IDs

**Claims System**
- Check coverage eligibility
- Create claim records
- Track claim status
- Update customer on progress

**CRM Integration**
- User profile data
- Interaction history
- Preferences and settings
- Opt-in/opt-out status

**Payment Gateway**
- Policy renewals
- Plan upgrades
- Payment status checks

**Analytics Platform**
- User journey tracking
- Button click analytics
- Drop-off points
- Conversion funnel
- Popular resources

### 10.3 State Management

**Conversation Context:**
```json
{
  "user_id": "91XXXXXXXXXX",
  "session_id": "sess_12345",
  "current_flow": "incident_reporting",
  "current_step": "safety_procedure_step_3",
  "incident_data": {
    "type": "otp_scam",
    "severity": "critical",
    "amount": 45000,
    "timestamp": "2025-11-18T10:30:00Z"
  },
  "temp_data": {
    "answers": {},
    "uploads": []
  },
  "last_message_time": "2025-11-18T10:32:15Z"
}
```

**Session Timeout:**
- 30 minutes of inactivity → Save state, end session
- User returns → Resume from saved state
- Option to start fresh

### 10.4 Webhook Events to Handle

**Inbound Messages:**
- `message` → User sent text
- `button_reply` → User clicked button
- `list_reply` → User selected from list
- `quick_reply` → User clicked quick reply
- `media` → User uploaded image/video/document
- `location` → User shared location

**Outbound Message Status:**
- `sent` → Delivered to WhatsApp
- `delivered` → Delivered to user's device
- `read` → User opened message
- `failed` → Delivery failed (handle retry)

**System Events:**
- User blocks bot → Log, update CRM
- User unblocks bot → Resume service
- 24-hour window expires → Switch to template messages

### 10.5 Error Handling

**User Input Errors:**
```
Bot: Hmm, I didn't quite get that. 🤔

Could you please:

[Button: 🔄 Try Again]
[Button: 💬 Explain Differently]
[Button: 👤 Talk to Human]
[Button: 🏠 Main Menu]
```

**System Errors:**
```
Bot: Oops! Something went wrong on our end. 😕

Don't worry, your data is safe. Let's try again.

[Button: 🔄 Retry]
[Button: 📞 Call Support]
[Button: 💾 Save & Continue Later]

If this persists, please call: 1800-XXX-XXXX
```

**Timeout/Abandoned Flow:**
```
Bot: I noticed we got disconnected earlier. 

Would you like to:

[Button: ▶️ Continue Where We Left Off]
[Button: 🔄 Start Fresh]
[Button: 💬 Talk to Agent]
[Button: 🏠 Main Menu]
```

### 10.6 Analytics & Metrics

**Track:**
- Total messages sent/received
- Active users (daily/weekly/monthly)
- Conversation completion rate
- Button click through rate
- Most used flows
- Average conversation duration
- Escalation to human agent rate
- Incident report completion rate
- Educational resource engagement
- User satisfaction scores

**Optimize:**
- A/B test message variants
- Refine button labels
- Simplify complex flows
- Improve error messages
- Reduce friction points

---

## 11. Best Practices & Guidelines

### Message Design

**✅ DO:**
- Keep messages short (1-3 sentences)
- Use emojis for visual hierarchy
- Provide clear next actions
- Use buttons for primary actions
- Show progress in multi-step flows
- Confirm important actions

**❌ DON'T:**
- Send long paragraphs
- Use too many emojis (overwhelming)
- Ask open-ended questions (use buttons/quick replies)
- Make assumptions about user knowledge
- Hide the "back" option
- Use technical jargon

### Tone & Voice

**Empathetic:** Acknowledge stress of cyber incidents
**Clear:** Simple language, no jargon
**Reassuring:** "You did the right thing by reporting"
**Professional:** Trustworthy, not casual
**Friendly:** Warm, not robotic
**Action-oriented:** Guide to next steps

### Timing

**Response Time:** < 3 seconds for bot responses
**Human Handoff:** < 2 minutes during business hours
**Proactive Messages:** 
- Morning (10 AM) for check-ins
- Evening (6 PM) for reminders
- Avoid late night (10 PM - 8 AM)

### Privacy & Security

**Never ask for:**
- Full passwords/PINs
- CVV numbers
- OTPs
- Full card numbers

**Always:**
- Use masked data (last 4 digits only)
- Encrypt uploads
- Clear sensitive data after session
- Comply with DPDP Act

---

## 12. Future Enhancements

### Phase 2 Features
- Voice messages (report incident via voice)
- AI-powered image analysis (auto-extract info from screenshots)
- Chatbot-to-chatbot transfer (WhatsApp ↔ Stella seamless)
- Group chat support (family plans)
- WhatsApp Pay integration (premium payment)

### Phase 3 Features
- Proactive fraud detection (analyze user's messages for scam indicators)
- Personalized scam alerts based on user behavior
- Gamification (badges, streaks for completing courses)
- Community features (share warnings with friends)
- Multi-language support (Hindi, Tamil, Telugu, Bengali)

---

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Maintained By:** Boxx Insurance Product Team  
**Next Review:** December 2025

---

## Appendix: Sample Complete User Journey

### Scenario: User Reports OTP Scam

```
[User initiates chat]

Bot: Hi there! 👋

Welcome to Boxx Insurance. I'm here to help you with cyber 
incidents and protection.

What brings you here today?

[Button: 🚨 Report Cyber Incident] ← USER CLICKS
[Button: 📚 Learn About Cyber Safety]
[Button: 📋 My Insurance Info]
[Button: 💬 Talk to Support]

---

Bot: 🚨 REPORT CYBER INCIDENT

I'm here to help. First, what happened?

Select the situation closest to yours:

[List Item 1: 💸 Someone Got My Money] ← USER SELECTS
[List Item 2: 🔐 My Account Was Hacked]
[List Item 3: 📱 Suspicious Call/Message]
[List Item 4: 💻 Computer Problem]
[List Item 5: 🆔 Identity Misuse]
[List Item 6: 🤔 I'm Not Sure]

---

Bot: 💸 MONEY LOST

Which of these happened?

[Button: 📲 I gave away my OTP] ← USER CLICKS
[Button: 💳 Card details were used]
[Button: 🏦 Unauthorized bank transfer]
[Button: 🛒 Fake online shopping]

---

Bot: When did this happen?

[Quick Reply: Just now (< 1 hour)] ← USER CLICKS
[Quick Reply: Today]
[Quick Reply: Yesterday]

---

Bot: How much money was taken?

[Quick Reply: Less than ₹5,000]
[Quick Reply: ₹5,000 - ₹25,000]
[Quick Reply: ₹25,000 - ₹1,00,000] ← USER CLICKS

---

Bot: Do you still have access to your UPI/banking app?

[Quick Reply: Yes] ← USER CLICKS
[Quick Reply: No, can't login]

---

Bot: 🚨 URGENT ACTION NEEDED

Based on what you shared, we need to secure your account RIGHT NOW.

I'll guide you step by step. Ready?

[Button: ✅ Yes, Let's Start] ← USER CLICKS
[Button: 📞 Call Me Instead]

---

Bot: 🔒 STEP 1 of 5

Open your PhonePe app right now.

Done?

[Button: ✅ Done, Next Step] ← USER CLICKS
[Button: ❌ Can't Find It]

---

Bot: 🔒 STEP 2 of 5

Look for 'Block UPI' or 'Freeze Payments' in Settings.

Found it?

[Button: ✅ Yes, Found It] ← USER CLICKS
[Button: ❌ Don't See This Option]

---

[... continues through all 5 steps ...]

---

Bot: ✅ ACCOUNT SECURED!

Great job! Your account is now protected.

Next, I need some evidence to process your claim.

Please upload screenshots of the scam messages.

[Button: 📷 Take Photo] ← USER UPLOADS 2 IMAGES
[Button: 📁 Upload from Gallery]

---

Bot: ✅ Received Image 1
✅ Received Image 2

Upload more?

[Button: 📷 Upload Another]
[Button: ✅ That's All] ← USER CLICKS

---

Bot: 📋 INCIDENT SUMMARY

Review your report:

📌 Type: UPI OTP Scam
🕐 When: Just now
💰 Amount: ₹45,000
🏦 Bank/App: PhonePe
📎 Evidence: 2 files attached
🔒 Safety: Account secured ✅

Everything correct?

[Button: ✅ Submit Report] ← USER CLICKS
[Button: ✏️ Edit Details]

---

Bot: ✅ REPORT SUBMITTED

Incident ID: C-48271

📧 Confirmation sent to your email
📱 SMS sent with details

What happens next:
1. Claims team reviews (within 24 hrs)
2. They may contact you for more info
3. You'll get updates via WhatsApp

[Button: 📊 View Coverage] ← USER CLICKS
[Button: 💬 Stella (Wellness Support)]
[Button: 🏠 Main Menu]

---

Bot: 🛡️ YOUR COVERAGE

Good news! This incident is COVERED ✅

Your Plan: Individual Protection
Max Coverage: ₹1,00,000
This Incident: ₹45,000 claimed

📋 What's covered:
• Financial loss up to limit
• Professional recovery assistance

⏱️ Claim Timeline:
• Review: 24-48 hours
• Decision: 7-10 days
• Payout: 3-5 days after approval

[Button: 📄 View Full Policy]
[Button: 💬 Ask Claims Question]
[Button: ✅ Got It] ← USER CLICKS

---

Bot: 🧘 HOW ARE YOU FEELING?

Cyber incidents can be stressful. It's normal to feel:
• Anxious 😰
• Angry 😤
• Embarrassed 😳

Our wellness assistant Stella can help you process these feelings.

[Button: 💚 Talk to Stella]
[Button: 📚 Read Self-Help Tips]
[Button: ✅ I'm Okay] ← USER CLICKS

---

Bot: 📋 NEXT STEPS

Here's what you should do:

☐ File Police Complaint
☐ Report on Cybercrime Portal
☐ Block Scammer Number
☐ Change Passwords
☐ Download Boxx App

[Button: ✅ Done with Everything] ← USER CLICKS

---

Bot: Thank you, [Name]! 

Your incident is being processed. We'll keep you updated via WhatsApp.

Is there anything else I can help you with?

[Button: 📚 Learn How to Prevent This]
[Button: 🏠 Main Menu]
[Button: ✅ I'm Done]

[JOURNEY COMPLETE]
```

---

**Total Time:** ~8 minutes  
**User Satisfaction:** High (incident reported, account secured, emotionally supported)  
**Next Touchpoint:** Daily check-in at 10 AM next day

