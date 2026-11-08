from pathlib import Path
import json, re
root=Path(__file__).resolve().parent.parent
posts=[]
for path in sorted((root/'posts').glob('*.md')):
    text=path.read_text(encoding='utf-8')
    match=re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$',text,re.S)
    if not match: continue
    meta={}
    for line in match.group(1).splitlines():
        if ':' not in line: continue
        k,v=line.split(':',1)
        v=v.strip().strip('\"').strip("'")
        meta[k.strip()]=v
    if meta.get('published','true').lower()=='false': continue
    posts.append({**meta,'published':True,'slug':path.stem,'body':match.group(2)})
(root/'posts.json').write_text(json.dumps(posts,ensure_ascii=False),encoding='utf-8')
print(f'Built {len(posts)} posts')
