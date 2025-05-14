import os
import openai
import tweepy
from datetime import datetime

# Load API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def generate_quote():
    prompt = (
        "Write a short, tweet-length, original motivational quote in a bold tone. "
        "Themes: self-worth, glow-up, silence, money moves, Kenyan hustle, purpose. "
        "Target: Gen Z & Millennials in urban Africa. Include some slang or street wisdom."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=60,
        temperature=0.8
    )
    return response['choices'][0]['message']['content'].strip()

def post_to_twitter():
    quote = generate_quote()
    try:
        api.update_status(quote)
        print(f"[{datetime.now()}] Tweeted: {quote}")
    except Exception as e:
        print("Failed to post:", e)

# Run
post_to_twitter()
