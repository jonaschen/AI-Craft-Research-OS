"""Opt-in network check; does not update source records or download into the repo."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

failed = []
for source in json.loads(Path(__file__).with_name('sources.json').read_text()):
    try:
        with urlopen(source['url'], timeout=30) as response:
            digest = hashlib.sha256(response.read()).hexdigest()
        if digest != source['sha256']:
            raise ValueError('upstream bytes changed')
        print(source['id'], 'OK')
    except Exception as exc:
        failed.append(source['id'])
        print(source['id'], str(exc))
raise SystemExit(bool(failed))
