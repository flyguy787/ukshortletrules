# ---- Per-page sitemap <lastmod> (exec'd at the very end of build.py, after clean URLs) ----
# A page's date moves only when its <main> content changes (nav/footer/head-only edits don't count).
# State lives in lastmod.json: {file: {"h": sha256 of normalised <main>, "d": "YYYY-MM-DD"}}.
import hashlib, datetime, zoneinfo
def _main_hash(t):
    m=re.search(r'<main\b.*?</main>',t,re.S)
    s=m.group(0) if m else t
    s=re.sub(r'(href=["\'][^"\']*?)\.html(?=["\'#?])',r'\1',s)  # pre-clean-URL revisions hash the same
    s=re.sub(r'\s+',' ',s).strip()
    return hashlib.sha256(s.encode()).hexdigest()
def _loc(f):
    u=f[:-len('index.html')] if f.endswith('index.html') else (f[:-5] if f.endswith('.html') else f)
    return SITE+u
_LM=json.load(open('lastmod.json')) if os.path.exists('lastmod.json') else {}
_today=datetime.datetime.now(zoneinfo.ZoneInfo('Europe/London')).date().isoformat()
_new={}
for _f in PAGES:
    _h=_main_hash(open(_f).read());_o=_LM.get(_f)
    _new[_f]=_o if _o and _o['h']==_h else {'h':_h,'d':_today}
open('lastmod.json','w').write(json.dumps(_new,indent=1,sort_keys=True)+'\n')
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{_loc(f)}</loc><lastmod>{_new[f]["d"]}</lastmod></url>\n' for f in PAGES)+'</urlset>\n')
assert '.html' not in open('sitemap.xml').read()
