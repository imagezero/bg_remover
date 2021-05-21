import requests
import fire


ak = "ak-github"


url = "https://api.boring-images.ml/v1.0/transparent-net?api_key=ak-github"


def run(file, o=""):
    """
    python cli.py 1.jpeg --o=2.jpeg

    python cli.py --file=1.jpeg --o=2.jpeg

    python cli.py 1.jpeg
    """
    ext = "jpeg" if ".png" not in file else "png"
    files = {"file": (f"name.{ext}", open(file, "rb"), f"image/{ext}")}

    response = requests.request(
        "POST",
        url,
        files=files,
    )

    print(response.json(), response.elapsed.total_seconds())
    img = response.json()["result"]
    if o:
        with open(o, "wb") as fp:
            b = fp.write(requests.get(img).content)
            print(f"Wrote {b} bytes to {o}")
    return img


def entrypoint():
    fire.Fire(run)


if __name__ == "__main__":
    entrypoint()
