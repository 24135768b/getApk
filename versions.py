from google_play_scraper import app

# Read the app list from 'applist.txt'
with open("packages.txt", 'r', encoding='utf8') as f:
    app_list = [line.strip() for line in f.readlines()]

# Open 'version.txt' to write versions or errors
with open("version.txt", 'w', encoding='utf8') as o:
    for app_id in app_list:
        try:
            # Scrape the app data from Google Play
            result = app(app_id, lang='tw', country='tw')
            # Try to write the version to the file
            o.write(result['version'] + '\n')
        except Exception as e:
            # If an error occurs, write an error message
            o.write(f"Error with {app_id}: {str(e)}\n")