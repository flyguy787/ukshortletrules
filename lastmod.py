# ---- Per-page sitemap <lastmod> (exec'd at the very end of build.py, after clean URLs) ----
# A page's date moves when its <main> content or its search snippet (<title> + meta description) changes; nav/footer/other head edits don't count.
# State lives in lastmod.json: {file: {"h": sha256 of normalised <main>, "m": sha256 of title+description, "d": "YYYY-MM-DD"}}.
# An entry without "m" (written before 1 Nov 2026) just records it without moving the date.
import hashlib, datetime, zoneinfo
def _main_hash(t):
    m=re.search(r'<main\b.*?</main>',t,re.S)
    s=m.group(0) if m else t
    s=re.sub(r'(href=["\'][^"\']*?)\.html(?=["\'#?])',r'\1',s)  # pre-clean-URL revisions hash the same
    s=re.sub(r'\s+',' ',s).strip()
    return hashlib.sha256(s.encode()).hexdigest()
def _meta_hash(t):
    a=re.search(r'<title>(.*?)</title>',t,re.S);b=re.search(r'<meta name="description" content="([^"]*)"',t)
    return hashlib.sha256(((a.group(1) if a else '')+'\n'+(b.group(1) if b else '')).encode()).hexdigest()
def _loc(f):
    u=f[:-len('index.html')] if f.endswith('index.html') else (f[:-5] if f.endswith('.html') else f)
    return SITE+u
_LM=json.load(open('lastmod.json')) if os.path.exists('lastmod.json') else {}
_today=datetime.datetime.now(zoneinfo.ZoneInfo('Europe/London')).date().isoformat()
_new={}
for _f in PAGES:
    _t=open(_f).read();_h=_main_hash(_t);_m=_meta_hash(_t);_o=_LM.get(_f)
    _new[_f]={'h':_h,'m':_m,'d':_o['d']} if _o and _o['h']==_h and _o.get('m',_m)==_m else {'h':_h,'m':_m,'d':_today}
open('lastmod.json','w').write(json.dumps(_new,indent=1,sort_keys=True)+'\n')
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{_loc(f)}</loc><lastmod>{_new[f]["d"]}</lastmod></url>\n' for f in PAGES)+'</urlset>\n')
assert '.html' not in open('sitemap.xml').read()
