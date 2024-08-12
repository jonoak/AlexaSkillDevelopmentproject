# Alexa Skill: Task Manager

## Overview
This Alexa Skill allows users to manage their daily tasks and set reminders using voice commands. It integrates with external services like Google Calendar to manage reminders.

## Technical Details
- **Language:** Python
- **API:** Alexa Skills Kit (ASK), AWS Lambda for serverless deployment
- **Integration:** Google Calendar API for setting reminders

## Setup Instructions

### Prerequisites
- Amazon Developer Account
- AWS Account
- Python 3.8 or later
- AWS CLI configured with your account

### Step 1: Clone the repository

```bash
git clone https://github.com/your-repo/task-manager-alexa-skill.git
cd task-manager-alexa-skill
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set up AWS Lambda

1. Log in to your AWS account and go to the Lambda Console.
2. Create a new function with Python 3.8 as the runtime.
3. Upload the `lambda_function.py` file to the function code.
4. Deploy the function and note the ARN.

### Step 4: Create the Alexa Skill

1. Log in to the [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask).
2. Create a new skill and set the invocation name to "task manager".
3. Upload the `skill.json` and `models/en-US.json` files.
4. Set the endpoint to the ARN from your Lambda function.
5. Test the skill using the Alexa simulator.

## Challenges and Solutions
- **Natural Language Understanding:** Implemented custom slot types and extensive user testing.
- **Integration with External APIs:** Used the Google Calendar API for setting reminders.

## License
This project is licensed under the MIT License.
