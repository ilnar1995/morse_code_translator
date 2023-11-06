import requests
from PIL import Image
from io import BytesIO


def download_and_convert_image(url, output_path):
    # Загружаем изображение по URL
    response = requests.get(url)

    # Создаем объект изображения из полученных данных
    image = Image.open(BytesIO(response.content))

    # Преобразуем изображение в формат JPG
    image = image.convert("RGB")

    # Масштабируем изображение, если необходимо
    max_size = 1000
    if max(image.size) > max_size:
        image.thumbnail((max_size, max_size))

    # Сохраняем изображение на диск
    image.save(output_path, "JPEG")

    print(f"Изображение сохранено по пути: {output_path}")


# Пример использования функции
urls = [
    "https://proprikol.ru/wp-content/uploads/2020/04/krasivye-kartinki-vysokogo-razresheniya-3.jpg",
    "https://klike.net/uploads/posts/2023-02/1675839044_3-490.jpg"
]
output_path = "{}.jpg"
for index, url in enumerate(urls):
    download_and_convert_image(url, output_path.format(index + 1))
