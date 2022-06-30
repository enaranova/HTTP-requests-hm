import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, params=params, headers=headers)
        pprint(response.json())
        return response.json()

    def upload(self, file_path, filename):
        response_href = self._get_upload_link(file_path=file_path)
        url = response_href.get("href", "")
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_path = "..."
    filename = "..."
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(file_path, filename)