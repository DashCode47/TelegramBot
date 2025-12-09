# Deploy Telegram Bot to Cloud

This guide will help you deploy your Telegram job filter bot to Railway (free tier) or Render.

## 🚀 Option 1: Railway (Recommended - Free Tier Available)

### Steps:

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo" (or upload files)

3. **Configure Environment**
   - Railway will auto-detect Python
   - Add these environment variables in Settings → Variables:
     - `API_ID`: Your Telegram API ID (23002451)
     - `API_HASH`: Your Telegram API Hash
   
4. **Deploy**
   - Railway will automatically deploy
   - Check logs for authentication prompt
   - You'll need to authenticate once (phone + code)

5. **Keep Session File**
   - The session file will be stored in Railway's filesystem
   - It persists between restarts

### Note: First-time authentication
- Check Railway logs
- Enter your phone number when prompted
- Enter verification code
- After that, it runs automatically

---

## 🚀 Option 2: Render (Free Tier Available)

### Steps:

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Or upload files manually

3. **Configure**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python job_filter_bot.py`
   - **Environment**: Python 3
   - Add environment variables:
     - `API_ID`: Your Telegram API ID
     - `API_HASH`: Your Telegram API Hash

4. **Deploy**
   - Render will deploy automatically
   - Check logs for authentication

---

## 🔒 Security Note

**IMPORTANT**: Before deploying, move your API credentials to environment variables!

Update `job_filter_bot.py` to use environment variables:

```python
import os
api_id = int(os.getenv('API_ID', '23002451'))
api_hash = os.getenv('API_HASH', 'your_api_hash')
```

This keeps your credentials secure and out of your code.

---

## 📝 Alternative: Keep Running Locally (Background)

If you prefer to keep it on your computer but not visible:

**Windows:**
- Run as a background service
- Or use Task Scheduler to start on boot

**Mac/Linux:**
- Use `nohup` or `screen`/`tmux`
- Or create a systemd service

Would you like me to set up the environment variable version for secure deployment?

