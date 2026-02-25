import datetime

def format_timestamp(timestamp):
    # Convert UNIX timestamp to human-readable format
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
