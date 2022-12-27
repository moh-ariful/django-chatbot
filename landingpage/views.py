from django.shortcuts import render
import requests
import openai
openai.api_key = "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"


def index(request):
    # Pastikan untuk mengganti `api_key` dengan API key yang Anda miliki
    api_key = "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"
    headers = {"Authorization": f"Bearer {api_key}"}
    endpoint = "https://api.openai.com/v1/images/generations"

    # Buat payload yang akan dikirimkan bersama dengan permintaan
    # Anda dapat memodifikasi payload ini sesuai dengan kebutuhan aplikasi Anda
    data = {
        "model": "image-alpha-001",
        "prompt": "Beberapa orang duduk bersama melakukan meeting serius",
        "num_images": 1,
        "size": "256x256",
        "response_format": "url"
    }

    # Kirim permintaan ke API OpenAI dengan menggunakan method POST
    response = requests.post(endpoint, headers=headers, json=data)

    # Cek apakah permintaan berhasil atau tidak dengan mengecek status code respon
    if response.status_code == 200:
        # Jika permintaan berhasil, ambil URL gambar yang dihasilkan oleh API dari respon
        image_url = response.json()["data"][0]["url"]
    else:
        # Jika permintaan gagal, tampilkan pesan error
        image_url = "Error generating image"

    # Tampilkan halaman index.html dengan menggunakan context yang menyertakan URL gambar
    return render(request, "index.html", {"image_url": image_url})


def diskusi(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        model_engine = "text-davinci-002"

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return render(request, "diskusi.html", {"message": message})
    else:
        return render(request, "diskusi.html")
