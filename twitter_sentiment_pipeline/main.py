from src.twitter_stream import stream_tweets
from src.sentiment_infer import classify_stream
from src.dashboard import launch_dashboard

if __name__ == "__main__":
    print("🚀 Starting Real-Time Sentiment Analysis Pipeline...")
    stream_tweets(track_terms=["AI", "Technology", "Startups"])
    classify_stream()
    launch_dashboard()
