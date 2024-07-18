# tts_app/views.py
from django.shortcuts import render
import requests
import json


def tts_form(request):
    result = None
    audio_link = None  # Khởi tạo biến audio_link
    if request.method == "POST":
        text = request.POST.get('text')
        voice = request.POST.get('voice')
        speed = request.POST.get('speed')

        # API endpoint và payload
        url = "https://api.idg.vnpt.vn/tts-service/v2/grpc"
        payload = json.dumps({
            "text": text,
            "text_split": "false",
            "speed": speed,
            "region": voice
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxYzVhYzI3Yy05OGM3LTFhMzktZTA2My02MzE5OWYwYTkyOWQiLCJhdWQiOlsicmVzdHNlcnZpY2UiXSwidXNlcl9uYW1lIjoiaG9hbmdhYXRyb3gyMzUwNEBnbWFpbC5jb20iLCJzY29wZSI6WyJyZWFkIl0sImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0IiwibmFtZSI6ImhvYW5nYWF0cm94MjM1MDRAZ21haWwuY29tIiwidXVpZF9hY2NvdW50IjoiMWM1YWMyN2MtOThjNy0xYTM5LWUwNjMtNjMxOTlmMGE5MjlkIiwiYXV0aG9yaXRpZXMiOlsiVVNFUiJdLCJqdGkiOiJhNzBjNWQyMy03MDBhLTQ3ZTgtOThjMC02ZGZmMTgxMTZiOGUiLCJjbGllbnRfaWQiOiJhZG1pbmFwcCJ9.pmPH7ts8jkWcOu1qZ0g0yMUA0tRUexS3tZHEuSY5LMX8MfVzZeATQD6q6eysvuTQgOr1gte6F2N729pnrcqbHTldCBJsv1cJJKFmkxLD2leGb6bFd4uEoBPpaUAcWr6GhkKFBjLWsBZDTu2d4xAcdiHxaKIMMG2qyWG18fXKEJ_bkyt7gkZL1Wh8i5Ic6bHVWq-VRal6Td128RLNxIhT4V0vLbW7-2V-yxHfa6YS7N9lfWq1Hru5ieD1ogmcsGcMxmdEBI9S3bC0W5oUDtAcRJyGxxAvX_ctHj3TQRpMEnT1G8ol9jhRGV1lDoDW26fGUoGXJbfWX0Rge8UR9SpomQ',
            'Token-id': '1c5ac405-1919-0ac1-e063-63199f0ac402',
            'Token-key': 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKj15ikj3q4kNESLkfLrJzGAOFsiScOw3iByTrhj8+c3HAnIGMZ9m+lQFUkfBOuTOdgNQdyA8ReoQniKKWZM63sCAwEAAQ=='
        }

        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            response_json = response.json()
            audio_link = response_json.get('object').get('playlist')[0].get(
                'audio_link')  # Lấy audio_link từ JSON response
            result = json.dumps(response_json, indent=4, ensure_ascii=False)
        else:
            result = f"Error: {response.status_code}\n{response.text}"

            return render(request, 'home.html', {'result': result, 'audio_link': audio_link})

    return render(request, 'tts_form.html', {'result': result, 'audio_link': audio_link})


def home(request):
    return render(request, 'home.html')

# Create your views here.
