# ---- Guides hub (/guides): every guide and free tool, grouped by nation. Titles = each page's H1, descriptions = its own meta description ----
import html as _H
def _gmeta(fn):
    t=open(fn).read()
    h=re.search(r'<h1>(.*?)</h1>',t,re.S);m=re.search(r'<meta name="description" content="([^"]*)">',t)
    return _H.unescape(re.sub(r'<[^>]+>','',h.group(1)).strip()),_H.unescape(m.group(1))
GHUB=[('England',['england-holiday-let-planning-permission.html','england-second-homes-council-tax-premium.html','holiday-let-fire-safety-england.html'],['london-90-night-counter.html'],'england.html'),
 ('Wales',['wales-second-homes-council-tax-premium.html','holiday-let-fire-safety-wales.html'],['wales-registration-checker.html'],'wales.html'),
 ('Scotland',['scotland-short-term-let-licence-guide.html','short-term-let-fire-safety-scotland.html'],['scotland-short-term-let-licence-fees.html','scotland-licence-renewal-checker.html','scotland-business-rates-checker.html'],'scotland.html'),
 ('Northern Ireland',['northern-ireland-tourism-certificate-guide.html'],[],'northern-ireland.html'),
 ('UK-wide',['holiday-let-tax-after-fhl-abolition.html'],['checker.html','uk-visitor-levy-map.html','levy-calculator.html','occupancy-threshold-tracker.html','buyer-due-diligence-checker.html','deadlines.html'],None)]
assert {u for _,u in GUIDES_NAV}=={g for _,G,_,_ in GHUB for g in G},'nav Guides and hub guide lists differ'
_gli=lambda fs:'<ul class="ghub">'+''.join((lambda tt,dd_:f'<li><a href="{fn}"><b>{e(tt)}</b></a><br><span class="small">{e(dd_)}</span></li>')(*_gmeta(fn)) for fn in fs)+'</ul>'
_gb='';_items=[]
for nm,G,T,nf in GHUB:
    _gid=re.sub(r'[^a-z]+','-',nm.lower()).strip('-')
    _gb+=f'<section aria-labelledby="g-{_gid}"><h2 id="g-{_gid}">{e(nm)}</h2>'
    if G:_gb+=('<h3>Guides</h3>' if T else '')+_gli(G)
    if T:_gb+='<h3>Free tools</h3>'+_gli(T)
    if nf:_gb+=f'<p><a href="{nf}">All {e(nm)} rules</a></p>'
    _gb+='</section>'
    _items+=[(fn,_gmeta(fn)[0]) for fn in G+T]
_gf='guides.html';_gt='Guides and free tools for UK short-let hosts'
_gd='Every UK Short-Let Rules guide and free tool for holiday-let and short-term-let hosts, grouped by nation: planning, licensing, council tax premiums, fire safety, tax and visitor levies.'
_gld=json.dumps({'@context':'https://schema.org','@type':'CollectionPage','name':_gt,'description':_gd,'url':SITE+_gf,'mainEntity':{'@type':'ItemList','numberOfItems':len(_items),'itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'url':SITE+fn} for i,(fn,n) in enumerate(_items)]}}).replace('</','<\\/')
_gbody=(f'<p class="lead">Every plain-English guide and free tool on the site, grouped by nation. Each one links to its official sources.</p>'
 +f'<p class="small">Jump to: '+' · '.join(f'<a href="#g-{re.sub(r"[^a-z]+","-",nm.lower()).strip("-")}">{e(nm)}</a>' for nm,*_ in GHUB)+'</p>'
 +_gb+'<h2>More</h2><ul><li><a href="councils.html">All councils with local rules</a></li><li><a href="changes.html">Latest rule changes</a></li><li><a href="newsletter.html">Weekly "what changed" email</a></li></ul>'
 +'<p class="small">General information only, not legal or tax advice. The UK Short-Let Rules team</p>')
page(_gf,_gt,_gbody,desc=_gd,full_title=_gt+' | UK Short-Let Rules Tracker',head=OGT(_gf,_gt,_gd)+f'<script type="application/ld+json">{_gld}</script>')
