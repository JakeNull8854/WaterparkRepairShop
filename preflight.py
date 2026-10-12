import json
from pathlib import Path

root = Path(__file__).resolve().parent
integration = json.loads((root / 'sheets' / 'integration.json').read_text(encoding='utf-8'))
missing = [name for name in ('hostIntegration','companionIntegration') if integration.get(name) != 'verified']
if not integration.get('runtimeVerified'):
    missing.append('real in-game runtime verification')
if missing:
    print('NOT RELEASE READY: ' + ', '.join(missing))
    raise SystemExit(1)
print('Design integration flags pass; independently validate Melty recipe and actual gameplay before publishing.')
