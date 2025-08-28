# AWS EC2 Event-Driven Telegram Monitoring Bot

This project is an event-driven bot that monitors the health of AWS EC2 instances and sends real-time alerts to a Telegram bot. It uses AWS Lambda, CloudWatch Events, and Telegram Bot API.

## Features

- Monitors EC2 instance state changes
- Sends Telegram messages for start/stop/terminate events
- Serverless architecture using AWS Lambda

## Deployment

1. Set up your AWS Lambda function with the provided code.
2. Configure a CloudWatch rule to trigger the Lambda on EC2 state changes.
3. Set your Telegram bot token and chat ID as environment variables in Lambda.

## Environment Variables

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`# ec2_event_tele
