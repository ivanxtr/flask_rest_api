from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args =reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of video")
video_put_args.add_argument("views", type=str, help="views of video")
video_put_args.add_argument("likes", type=str, help="likes of video")

videos = {}

def abortVideos(video_id):
    if video_id not in videos:
        abort(404, message="Video id is not valid")

class Video(Resource):
    def get(self, video_id):
        abortVideos(video_id)
        return videos[video_id]
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)
