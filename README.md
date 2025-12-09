# Telegram Job Filter Bot 🤖

A Telegram bot that monitors job channels and filters messages based on keywords, sending matching job posts directly to your Saved Messages.

## Features

- ✅ Monitors multiple Telegram channels 24/7
- ✅ Filters messages by keywords (React, Frontend, JavaScript, etc.)
- ✅ Sends matching job posts to your Saved Messages
- ✅ Supports multiple channels simultaneously
- ✅ Word boundary matching to avoid false positives

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure

Edit `job_filter_bot.py`:

- Add your Telegram API credentials (or use environment variables)
- Add channels to monitor in `target_channels`
- Customize keywords in `keywords` list

### 3. Run

```bash
python job_filter_bot.py
```

On first run, you'll be prompted to:
- Enter your phone number
- Enter the verification code sent to Telegram

## Configuration

### Channels

Add channels to monitor in the `target_channels` list:

```python
target_channels = [
    '@JScript_jobs',
    '@Frontend_Jobs',
    '@Remoteit',
]
```

**Important:** You must be a member of all channels you want to monitor.

### Keywords

Customize keywords to filter:

```python
keywords = ['react', 'react native', 'frontend', 'javascript', 'desarrollador', 'developer']
```

## Deployment

This bot can be deployed to:
- **Railway** (recommended - free tier available)
- **Render** (free tier available)
- **Fly.io** (free tier available)

See `README_DEPLOY.md` for detailed deployment instructions.

## Security

- API credentials should be stored as environment variables in production
- Session files (`.session`) are automatically ignored by git
- Never commit your `API_ID` or `API_HASH` to public repositories

## How It Works

1. Bot connects to Telegram using your account
2. Monitors specified channels for new messages
3. Checks each message for keyword matches
4. Sends matching posts to your Saved Messages with:
   - Summary of matched keywords
   - Original message forwarded

## License

MIT

