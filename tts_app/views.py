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
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxZDU0YmNkYy1iZjA5LTJmZTctZTA2My02MjE5OWYwYTRiMDciLCJhdWQiOlsicmVzdHNlcnZpY2UiXSwidXNlcl9uYW1lIjoidGhpbmhudnBzMjk0MDhAZnB0LmVkdS52biIsInNjb3BlIjpbInJlYWQiXSwiaXNzIjoiaHR0cHM6Ly9sb2NhbGhvc3QiLCJuYW1lIjoidGhpbmhudnBzMjk0MDhAZnB0LmVkdS52biIsInV1aWRfYWNjb3VudCI6IjFkNTRiY2RjLWJmMDktMmZlNy1lMDYzLTYyMTk5ZjBhNGIwNyIsImF1dGhvcml0aWVzIjpbIlVTRVIiXSwianRpIjoiY2U0ODdmMmItOGJiYy00NTZiLTg2MWYtOTNlOTQ0YjA4OTg3IiwiY2xpZW50X2lkIjoiYWRtaW5hcHAifQ.Y-o49N-bKpwJsYsnwwm4pJQUoqi_wlfzuU2RiysJx9v9wndvSfuxqam1sl1Eu2ldRxCmY16TRtOmaipvnzimwdz7m_JkDg5MDrwN8nYHw30Ts8Ws1s6F2Yhc1b8LCpmd77q-6Dc6NDv6enUErd9EpHMZ45UGFDW1mHZVJQQ0pk9aoAQpvnrVlmTRRbESMFGsnQD16b6RYdJj29921oeH7jfxwm-yJMtsVbieGgTXGjk9EVWY5cO2H01b5c8ZYn9O306YhuOlvB1XM19-xsgFCrYa3C3iJ4Mz6TLJp6HY0DgVoQgJOjqzV260vMoEIE7xWMeWfO0obFARZHFpomnLyw',
            'Token-id': '1d54c078-af63-5cbb-e063-63199f0a8697',
            'Token-key': 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJmHrBW152nV+etQ0/o/fWeUKCu5ZyMCn/4ZIob+7X4REyVoMgu/d2DdBFEzTb5O1h7pr4oTlnlG5wQPMuidszsCAwEAAQ=='
        }

        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            response_json = response.json()
            audio_link = response_json.get('object').get('playlist')[0].get(
                'audio_link')  # Lấy audio_link từ JSON response
            result = json.dumps(response_json, indent=4, ensure_ascii=False)
        else:
            result = f"Error: {response.status_code}\n{response.text}"

            return render(request, 'about.html', {'result': result, 'audio_link': audio_link})

    return render(request, 'tts_form.html', {'result': result, 'audio_link': audio_link})


def about(request):
    return render(request, 'about.html')

# Create your views here.
