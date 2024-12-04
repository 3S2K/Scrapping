from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re


class YouTubeTranscriptExtractor:
    @staticmethod
    def get_youtube_video_id(url):
        video_id_match = re.search(r"(?:v=|youtu\.be/|embed/|shorts/)([a-zA-Z0-9_-]{11})", url)
        if video_id_match:
            return video_id_match.group(1)
        else:
            raise ValueError("유효한 YouTube URL이 아닙니다.")

    @staticmethod
    def fetch_youtube_captions(url):
        try:
            video_id = YouTubeTranscriptExtractor.get_youtube_video_id(url)
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            try:
                transcript = transcript_list.find_transcript(['ko', 'en'])
            except:
                transcript = transcript_list.find_manually_created_transcript(['en'])

            captions = transcript.fetch()

            # 자막 형식 변환
            formatter = TextFormatter()
            return formatter.format_transcript(captions)

        except Exception as e:
            return f"자막을 가져오는 중 오류 발생: {e}"

