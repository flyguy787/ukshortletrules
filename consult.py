# ---- /consultations: open and recently closed public consultations affecting UK short-term lets / holiday lets ----
# CONS data lives in consdata.py (shared with build.py CONSOPEN). Status is worked out at build time (Europe/London):
# a consultation moves to the archive the day after its closing date. Perth & Kinross is directory-only and is never listed.
# Each check is logged in /workspace/ukslr/SOURCE_LOG.csv (topic 'consultation check').
exec(open('consdata.py').read())
CONS_NEXT={('Argyll and Bute Council','Planning control area'):'findings go to a future council meeting; if approved, the Scottish Government would have to agree before it could start',
 ('Falkirk Council','Visitor levy'):'Full Council expected to decide in January 2027',
 ('Dundee City Council','Visitor levy'):'earliest a levy could apply is 2028/29',
 ('The Highland Council','Visitor levy'):'councillors could decide on 10 December 2026',
 ('Moray Council','Second homes council tax'):'report to Full Council in January 2027'}
def _cpk(c):return ('council:'+c['s'],c['w']) if c['s'] else ('nation:'+c['n'].lower().replace(' ','-'),c['n'])
assert not any('kinross' in (c['w']+c['s']+c['t']).lower() for c in CONS)
import datetime as _cdt
try:
    from zoneinfo import ZoneInfo as _CZ;_ctoday=_cdt.datetime.now(_CZ('Europe/London')).date()
except Exception:_ctoday=_cdt.date.today()
_cd=lambda s:_cdt.date.fromisoformat(s)
_cf=lambda s:_cd(s).strftime('%a %-d %b %Y')
_copen=sorted([c for c in CONS if _cd(c['c'])>=_ctoday],key=lambda c:c['c'])
_cclosed=sorted([c for c in CONS if _cd(c['c'])<_ctoday],key=lambda c:c['c'],reverse=True)
def _cwhere(c,link=True):
    if c['s'] and link:return f'<a href="councils/{c["s"]}.html">{e(c["w"])}</a> ({e(c["n"])})'
    return e(c['w']) if c['w']==('All of '+c['n']) else f'{e(c["w"])} ({e(c["n"])})'
def _ccard(c,op):
    dl=(_cd(c['c'])-_ctoday).days
    pill=('<span class="pill p-coming">Closes today</span>' if dl==0 else f'<span class="pill p-coming">{dl} day{"s" if dl!=1 else ""} left</span>') if op else '<span class="pill p-proposed">Closed</span>'
    rows=[('Who is consulting',e(c['b'])),('Where',_cwhere(c)),('Topic',e(c['k'])),
          ('Opened',_cf(c['o']) if c['o'] else e(c.get('on','not stated'))),
          ('Closes' if op else 'Closed',f'<b>{_cf(c["c"])}</b>'+(f' {e(c["cn"])}' if c['cn'] else ''))]
    if op:rows.append(('How to respond',c['r']))
    return (f'<article class="box cons" id="{"c-"+re.sub(r"[^a-z0-9]+","-",(c["b"]+" "+c["t"]).lower()).strip("-")[:60]}"><h3>{e(c["t"])} {pill}</h3>'
     +'<dl class="cdl">'+''.join(f'<dt>{a}</dt><dd>{v}</dd>' for a,v in rows)+'</dl>'
     +f'<p>{c["x"]}</p>'+((lambda a,nm:f'<p class="cpick"><a href="#cons-alerts" data-pick="{a}" data-cta="cons-card-pick">'+(f'Get an email when {e(nm)} decides' if a.startswith('council:') else f'Get an email when {e(nm)} short-let rules change')+'</a></p>')(*_cpk(c)) if op else '')+f'<p class="small"><a href="{c["u"]}" rel="nofollow">Official consultation page</a> · checked {CONS_CHECKED}</p></article>')
_csum=''.join(f'<tr><td><b>{_cd(c["c"]).strftime("%-d %b %Y")}</b></td><td>{_cwhere(c,False)}</td><td><a href="#{"c-"+re.sub(r"[^a-z0-9]+","-",(c["b"]+" "+c["t"]).lower()).strip("-")[:60]}">{e(c["t"])}</a></td><td>{e(c["k"])}</td></tr>' for c in _copen)
_cntw=len([c for c in _copen if (_cd(c['c'])-_ctoday).days<=14])
_cnx=[(c,CONS_NEXT.get((c['b'],c['k']))) for c in _copen]
CONSALERT=(PICK('consultations',aid='cons-alerts',tag='div')
 .replace('>Get free rule-change alerts for <span class="acn">your council</span></h2>','>Get an email when <span class="acn">your council</span> consults or decides</h2>',1)
 .replace('<p>Pick your council. We email you when its short-let rules change (licensing, planning, levy, fees), plus one short weekly "what changed" email. Free. Unsubscribe any time.</p>',
   '<p>Pick your council. We email you when a consultation or council decision changes its short-let rules (licensing, planning, visitor levy, council tax, fees). The weekly "what changed" email also lists consultations closing soon. Free. Unsubscribe any time.</p>',1)
 .replace('</script></div>','</script>'+(('<p class="anxh"><b>What happens after the open consultations close:</b></p><ul class="anx">'+''.join(f'<li><b>{e(c["w"])}</b> ({e(c["k"].lower())}, closes {_cd(c["c"]).strftime("%-d %b")}): {e(n)}</li>' for c,n in _cnx if n)+'</ul>') if any(n for c,n in _cnx) else '')+'</div>',1))
assert CONSALERT.index('</form>')<CONSALERT.index('What happens after') if 'What happens after' in CONSALERT else True
assert 'consults or decides' in CONSALERT and 'consultation or council decision' in CONSALERT
_cft='Short-let consultations: have your say before they close'
_cfd='Open UK short-let and holiday-let consultations: control areas, visitor levies, second home council tax and planning guidance, with closing dates and links.'
_cbody=(f'<p class="lead">Public consultations that could change the rules for short-term lets and holiday lets in England, Scotland, Wales and Northern Ireland, with closing dates and how to respond. Every detail comes from the official consultation page, linked on each one. Checked {CONS_CHECKED}.</p>'
 +(f'<div class="answer"><h2>Open now: {len(_copen)} consultation{"s" if len(_copen)!=1 else ""}</h2><p>'
   +(f'{_cntw} close{"s" if _cntw==1 else ""} within 14 days. ' if _cntw else '')
   +f'The next closes on <b>{_cf(_copen[0]["c"])}</b>: {e(_copen[0]["t"])} ({e(_copen[0]["b"])}).</p></div>' if _copen else '<div class="answer"><h2>No open consultations right now</h2><p>We have no open short-let consultations logged. The closed ones are in the archive below.</p></div>')
 +CONSALERT
 +(f'<h2 id="open">Open consultations, closing soonest first</h2><div class="tw"><table class="stk"><tr><th>Closes</th><th>Where</th><th>Consultation</th><th>Topic</th></tr>{_csum}</table></div>'
   +''.join(_ccard(c,True) for c in _copen) if _copen else '')
 +'<p>Closing dates also appear on the <a href="deadlines.html">UK short-let deadlines</a> page, alongside levy start dates and tax deadlines.</p>'
 +f'<h2 id="archive">Closed (archive)</h2><p>Consultations that have closed since late 2025, most recent first. We note the outcome where the official page gives one.</p>'
 +''.join(_ccard(c,False) for c in _cclosed)
 +'<h2>What we look for</h2><p>We check UK government, Scottish Government, Welsh Government and Northern Ireland Executive consultation pages, and council consultation hubs, for anything on short-term let licensing or registration, planning control areas and Article 4 directions, visitor levies, second home council tax premiums, business rates and fire safety. A consultation is only listed once we have read it on the official page. If a date or detail isn\'t on that page, we say "not stated".</p>'
 +'<p>Related: <a href="changes.html">Latest rule changes</a> · <a href="uk-visitor-levy-map.html">UK visitor levy map</a> · <a href="councils.html">All councils</a> · <a href="guides.html">Guides and free tools</a></p>'
 +'<p class="small">General information only, not legal or tax advice. Consultations can be extended or closed early, so check the official page before you rely on a date. The UK Short-Let Rules team</p>')
_cld=json.dumps({'@context':'https://schema.org','@type':'CollectionPage','name':_cft,'description':_cfd,'url':SITE+'consultations','dateModified':'2026-11-04'}).replace('</','<\\/')
page('consultations.html','Short-let consultations: open and closing soon',_cbody,desc=_cfd,full_title='UK Short-Let Consultations: Open Now and Closing Dates',head=OGT('consultations.html',_cft,_cfd)+f'<script type="application/ld+json">{_cld}</script>')
