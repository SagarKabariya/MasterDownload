from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

# Function to get direct Instagram video URL
def get_instagram_video_url(instagram_url):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(instagram_url, download=False)
        return info.get("url", None)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    instagram_url = data.get("url")

    if not instagram_url:
        return jsonify({"error": "No URL provided"}), 400

    video_url = get_instagram_video_url(instagram_url)
    if video_url:
        return jsonify({"video_url": video_url})
    else:
        return jsonify({"error": "Failed to fetch video"}), 500

if __name__ == '__main__':
    app.run(debug=True)
