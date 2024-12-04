import json
from Parsers.YouTubeParser import YouTubeTranscriptExtractor

with open('youtube_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# 3. 각 숏츠 링크에 접근하여 출력
for category, videos in data.items():
    for title, link in videos.items():
        captions = YouTubeTranscriptExtractor.fetch_youtube_captions(link)
        if captions:
            data[category][title] = captions
            print("수정되었습니다")


# 4. 수정된 데이터를 다시 JSON 파일로 저장
with open('youtube_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("JSON 파일이 성공적으로 수정되었습니다.")


