import os
import requests
import json

creds_dir = r"C:\Users\SURFACE LAPTOP\.gemini\antigravity\scratch\regan_costa_nursing_cv\public\credentials"
uploaded = {}

for f in sorted(os.listdir(creds_dir)):
    if f.endswith(".jpg"):
        path = os.path.join(creds_dir, f)
        try:
            with open(path, "rb") as fp:
                r = requests.post("https://freeimage.host/api/1/upload", 
                                  data={"key": "6d207e02198a847aa98d0a2a901485a5", "action": "upload", "format": "json"}, 
                                  files={"source": fp}, timeout=15)
                if r.status_code == 200:
                    data = r.json()
                    viewer = data["image"]["url_viewer"]
                    direct = data["image"]["url"]
                    uploaded[f] = {
                        "direct_url": direct,
                        "viewer_url": viewer
                    }
                    print("Uploaded", f, "->", viewer)
                else:
                    print("Failed", f, r.status_code, r.text[:100])
        except Exception as e:
            print("Error uploading", f, e)

out_file = r"C:\Users\SURFACE LAPTOP\.gemini\antigravity\scratch\regan_costa_nursing_cv\uploaded_links.json"
with open(out_file, "w") as out:
    json.dump(uploaded, out, indent=2)

print("\nSaved all cloud links to uploaded_links.json!")
