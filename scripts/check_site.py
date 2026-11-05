"""Check rendered internal URLs, anchors and accidental template content."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '_site')
base=sys.argv[2].rstrip('/') if len(sys.argv)>2 else ''
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.links=[]; self.ids=set(); self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        for key in ('src','href'):
            if key in a: self.links.append(a[key])
errors=[]
for file in root.rglob('*.html'):
    text=file.read_text(); page=Page(text)
    for marker in ('Lorem ipsum','YOUR_GOOGLE_SCHOLAR_ID','fetch_google_scholar','FastSpeech','{{','{%'):
        if marker in text: errors.append(f'{file}: leftover {marker}')
    for link in page.links:
        u=urlsplit(link)
        if u.scheme or u.netloc: continue
        path=unquote(u.path)
        if base and path.startswith(base+'/'): path=path[len(base):]
        target=(root/path.lstrip('/')) if path.startswith('/') else (file.parent/path if path else file)
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(f'{file}: missing {link}')
        elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in Page(target.read_text()).ids:
            errors.append(f'{file}: missing anchor {link}')
if errors: print('\n'.join(errors)); sys.exit(1)
print('PASS: rendered local assets, links, anchors and template-content checks')
