import pathlib
import secrets
import aiohttp
import aiofiles
from quart import Quart, jsonify, send_from_directory, url_for, request, render_template
import random
import os
import quart.flask_patch    


app = Quart(__name__)



@app.route("/")
async def home():
    return f"""
    {request.method}
    {request.url_rule}
    
    """

@app.route("/search/<filename>")
async def search(filename):
    dir = "/root/yanpdb/nsfw_cdn/"
    p = pathlib.Path(dir)


    for f in p.rglob(filename):
        print(str(f.parent))

    

    if f.parent == pathlib.Path("/root/yanpdb/nsfw_cdn/images/hentai"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/hentai", image=f"https://i.thino.pics/{filename}", dir=f"{str(f.resolve)}")

    if f.parent == pathlib.Path("/root/yanpdb/nsfw_cdn/images/helltakerpics"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/helltaker", image=f"https://i.thino.pics/{filename}",dir=f"{str(f.resolve)}")

    if f.parent == pathlib.Path("/root/yanpdb/nsfw_cdn/images/neko"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/neko", image=f"https://i.thino.pics/{filename}", dir=f"{str(f.resolve)}")

    if f.parent == pathlib.Path("/root/yanpdb/nsfw_cdn/images/tomboy"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/tomboy", image=f"https://i.thino.pics/{filename}", dir=f"{str(f.resolve)}")




@app.route('/<filename>')
async def sendfile(filename=None):
    dir = "/root/yanpdb/nsfw_cdn/"
    p = pathlib.Path(dir)
    for f in p.rglob(filename):
        pass
    
    print(filename)
    print(str(f.parent))

    return await send_from_directory(str(f.parent),filename)    

@app.route('/check', methods=['POST'])
async def uptime_check():
    return "Checked!"

if __name__ == "__main__":
    app.run(debug=True, port=2031)