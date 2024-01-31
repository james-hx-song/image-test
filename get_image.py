from streetview import search_panoramas, get_panorama
from flask import Flask, request, jsonify
import asyncio
import aiohttp

app = Flask(__name__)
# panos = search_panoramas(lat=41.8982208, lon=12.4764804)
# first = panos[0]
# image = get_panorama(pano_id=first.pano_id, zoom=1)
# image.save("test.jpg")


@app.route("/get_image/", methods=["POST"])
def send_image():
    data = request.json
    lat, lon, zoom = (
        float(data.get("lat", 41.8982208)),
        float(data.get("lon", 12.4764804)),
        int(data.get("zoom", 1)),
    )
    iter = int(data.get("iter", 3))
    asyncio.run(get_image(lat, lon, 1, zoom))
    return jsonify({"status": "ok"})


async def get_image(lat, lon, iter, zoom):
    async with aiohttp.ClientSession() as session:
        for i in range(iter):
            panos = search_panoramas(lat=lat + i / 100, lon=lon)
            for j in range(min(len(panos), iter)):
                image = get_panorama(pano_id=panos[j].pano_id, zoom=zoom)
                image.save(f"test{i}{j}_zoom{zoom}.jpg")

    # loop = asyncio.get_running_loop()
    # for i in range(5):
    #     panos = await loop.run_in_executor(None, search_panoramas, lat+i/100, lon)
    #     for j in range(min(len(panos), 5)):
    #         image = await loop.run_in_executor(None, get_panorama, panos[j].pano_id, 1)
    #         image.save(f"test{i}{j}.jpg")


if __name__ == "__main__":
    app.run(port=8000)
