#!/usr/bin/env python3
"""Baut das Kodi-Repository aus den Addon-Ordnern in diesem Repo.
Ausgabe: _site/ (wird von der GitHub Action auf den Branch gh-pages gelegt)
  _site/zips/addons.xml, addons.xml.md5, <id>/<id>-<version>.zip
  _site/index.html + repository-Zip im Wurzelverzeichnis (fuer "Aus ZIP installieren")
"""
import hashlib, os, re, shutil, zipfile, xml.etree.ElementTree as ET

ADDONS = ["skin.arctic.zephyr.modern", "repository.sunset1982"]
EXCLUDE = re.compile(r"(^|/)(\.git|\.DS_Store|Thumbs\.db|__pycache__)(/|$)|script-skinshortcuts-includes\.xml$")
OUT = "_site"

def build():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(f"{OUT}/zips")
    entries, repo_zip = [], None
    for aid in ADDONS:
        tree = ET.parse(f"{aid}/addon.xml"); root = tree.getroot()
        assert root.get("id") == aid, f"ID passt nicht: {aid}"
        ver = root.get("version")
        dst = f"{OUT}/zips/{aid}"; os.makedirs(dst)
        zpath = f"{dst}/{aid}-{ver}.zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for base, dirs, files in os.walk(aid):
                dirs.sort()
                for f in sorted(files):
                    full = os.path.join(base, f)
                    if EXCLUDE.search(full.replace(os.sep, "/")):
                        continue
                    z.write(full, full)
        for asset in ("icon.png", "fanart.jpg"):
            if os.path.exists(f"{aid}/{asset}"):
                shutil.copy(f"{aid}/{asset}", dst)
        xml = open(f"{aid}/addon.xml", encoding="utf-8").read()
        xml = re.sub(r"^<\?xml[^>]*\?>\s*", "", xml).strip()
        entries.append(xml)
        if aid.startswith("repository."):
            repo_zip = zpath
        print(f"{aid} {ver}: {os.path.getsize(zpath)/1e6:.1f} MB")
    addons_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n' + "\n\n".join(entries) + "\n</addons>\n"
    open(f"{OUT}/zips/addons.xml", "w", encoding="utf-8").write(addons_xml)
    md5 = hashlib.md5(addons_xml.encode("utf-8")).hexdigest()
    open(f"{OUT}/zips/addons.xml.md5", "w").write(md5)
    name = os.path.basename(repo_zip)
    shutil.copy(repo_zip, f"{OUT}/{name}")
    open(f"{OUT}/index.html", "w", encoding="utf-8").write(
        f'<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>Sunset1982 Kodi Repository</title></head>\n'
        f'<body>\n<h1>Sunset1982 Kodi Repository</h1>\n<a href="{name}">{name}</a>\n</body></html>\n')
    open(f"{OUT}/.nojekyll", "w").close()
    print("fertig:", OUT, "md5", md5)

if __name__ == "__main__":
    build()
