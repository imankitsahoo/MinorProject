import json
from googleapiclient.discovery import build

# Define API key (replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'AIzaSyAmEaRkMDE7inTQ3laxi8boiBtKbbfdNN0'

# Function to fetch YouTube video data
def fetch_youtube_data(query):
    # Build the YouTube API service
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Call the search.list method to search for videos based on the query
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=10  # Adjust as needed
    ).execute()

    # List to store video data
    video_data = []

    # Iterate over search results and extract video information
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']
            video_title = search_result['snippet']['title']
            video_description = search_result['snippet']['description']
            video_data.append({
                'video_id': video_id,
                'title': video_title,
                'description': video_description
            })
    
    return video_data

# Function to save data to a JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Main function
def main():
    # Fetch YouTube data based on the query
    query = input("Enter your search query: ")
    youtube_data = fetch_youtube_data(query)
    
    # Save the fetched data to a JSON file
    filename = 'youtube_data.json'
    save_to_json(youtube_data, filename)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()
