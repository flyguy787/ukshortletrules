# ---- Guides hub (/guides): every guide and free tool, grouped by nation. Titles = each page's H1, descriptions = its own meta description ----
import html as _H
def _gmeta(fn):
    t=open(fn).read()
    h=re.search(r'<h1>(.*?)</h1>',t,re.S);m=re.search(r'<meta name="description" content="([^"]*)">',t)
    return _H.unescape(re.sub(r'<[^>]+>','',h.group(1)).strip()),_H.unescape(m.group(1))
GHUB=[('England',['england-short-term-let-rules-2027.html','england-holiday-let-planning-permission.html','england-second-homes-council-tax-premium.html','holiday-let-fire-safety-england.html'],['london-90-night-counter.html'],'england.html'),
 ('Wales',['wales-second-homes-council-tax-premium.html','holiday-let-fire-safety-wales.html','wales-visitor-accommodation-licensing.html'],['wales-registration-checker.html'],'wales.html'),
 ('Scotland',['scotland-short-term-let-licence-guide.html','short-term-let-fire-safety-scotland.html'],['scotland-short-term-let-licence-fees.html','scotland-licence-renewal-checker.html','scotland-business-rates-checker.html'],'scotland.html'),
 ('Northern Ireland',['northern-ireland-tourism-certificate-guide.html'],[],'northern-ireland.html'),
 ('UK-wide',['holiday-let-tax-after-fhl-abolition.html','holiday-let-insurance-uk.html'],['checker.html','uk-visitor-levy-map.html','levy-calculator.html','occupancy-threshold-tracker.html','buyer-due-diligence-checker.html','deadlines.html'],None)]
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
# 'Rules in your council' block (growth push, 2 Nov): pick a council (council:<slug>) or a whole nation (nation:<id>) -> that area's one-line rule summary
# (data.json 'rule' / nation 'summary', already shown on /councils and the nation pages, with the council's official source), a link to its page,
# its next sourced key dates, and an in-context alert box pre-set to the pick (data-cta guides-council-result). Hides the sitewide box while shown.
# Perth & Kinross (PICK_EXCL) never appears. GA4: guides_council_pick {area_type, council}, once per distinct pick per page view.
_gcx={x['s']:x for x in V2D['councils']}
_gcd={'c':{},'n':{}}
_gco=''
for _n in d['nations']:
    _cs=sorted([c for c in d['councils'] if c['nation']==_n['name'] and c['verified'] and _sl(c) not in PICK_EXCL and _sl(c) in _gcx],key=lambda c:c['name'].replace('City of ',''))
    _gcd['n'][_n['id']]={'n':_n['name'],'r':_n['summary'],'u':_n['id']}
    _gco+=f'<optgroup label="{e(_n["name"])}"><option value="nation:{_n["id"]}">All of {e(_n["name"])}</option>'+''.join(f'<option value="council:{_sl(c)}">{e(c["name"])}</option>' for c in _cs)+'</optgroup>'
    for c in _cs:_gcd['c'][_sl(c)]={'n':c['name'],'r':c['rule'],'src':c['source'],'nx':_gcx[_sl(c)]['nx']}
assert not any('kinross' in k for k in _gcd['c']) and 'kinross' not in _gco.lower()
_GCJ=json.dumps(_gcd,ensure_ascii=False).replace('</','<\\/')
GCPICK=('<section class="box ghpick" id="g-council" aria-labelledby="gc-h"><h2 id="gc-h">Rules in your council</h2><p>Pick your council, or a whole nation, to see its short-let rules in brief, with a link to its full page and free alerts when they change.</p>'
 '<label for="gc-sel"><b>Your council</b></label><select id="gc-sel"><option value="">Choose your council</option>'+_gco+'</select>'
 '<div id="gc-res" hidden><h3 id="gc-n"></h3><p id="gc-r"></p><p class="small"><a id="gc-l" href="councils.html" data-cta="guides-council-page">Full rules</a><span id="gc-sw"> · <a id="gc-s" href="councils.html" rel="nofollow">Official source</a></span></p></div>'
 '<p class="small">Not listed? <a href="councils.html">Browse all councils</a>.</p></section>'
 '<div class="alertbox" id="gc-alert" hidden><h2>Get an email when short-let rules change in <span id="gc-an">your council</span></h2><p id="gc-why">We track these rules against official sources and email you when one of them changes.</p><p class="anxh" id="gc-nxh" hidden><b>Dates we\'re watching:</b></p><ul class="anx" id="gc-nx" hidden></ul><p class="small">Plus one short weekly UK "what changed" email. Free. Unsubscribe any time.</p>'
 +FORMX.replace('<form class="signup"','<form class="signup" id="gc-form" data-cta="guides-council-result" data-area="" data-area-name=""',1).replace('>Subscribe<','>Get free alerts<')+'</div>'
 '<script>(function(){var D='+_GCJ+r''',S=document.getElementById('gc-sel'),R=document.getElementById('gc-res'),A=document.getElementById('gc-alert'),F=document.getElementById('gc-form'),seen={};
function $(i){return document.getElementById(i)}
function sw(h){var W=document.querySelector('section.alertcta');if(W)W.hidden=h}
function go(ev){var v=S.value,m=v.match(/^(council|nation):(.+)$/),x=m&&(m[1]=='council'?D.c[m[2]]:D.n[m[2]]);
if(!x){R.hidden=true;A.hidden=true;sw(false);return}
var c=m[1]=='council';$('gc-n').textContent=c?x.n:'All of '+x.n;$('gc-r').textContent=x.r;var L=$('gc-l');L.href=c?'councils/'+m[2]:x.u;L.textContent=c?'Full '+x.n+' rules':'All '+x.n+' rules';
if(c&&x.src){$('gc-s').href=x.src;$('gc-sw').hidden=false}else $('gc-sw').hidden=true;R.hidden=false;
if(F.getAttribute('data-area')!=v){var M=F.querySelector('.msg');if(M)M.textContent=''}F.setAttribute('data-area',v);F.setAttribute('data-area-name',x.n);$('gc-an').textContent=c?x.n:'all of '+x.n;
$('gc-why').textContent=c?'We track licensing, planning, visitor levy and fee rules for '+x.n+' against official sources, and email you when one of them changes.':'We track the '+x.n+' rules against official sources and email you when one of them changes.';
var NX=$('gc-nx'),L2=c&&x.nx?x.nx:[];NX.innerHTML='';L2.forEach(function(t){var li=document.createElement('li');li.textContent=t;NX.appendChild(li)});NX.hidden=$('gc-nxh').hidden=!L2.length;
A.hidden=false;sw(true);if(ev&&!seen[v]){seen[v]=1;try{gtag('event','guides_council_pick',{area_type:m[1],council:m[2]})}catch(e){}}}
S.addEventListener('change',go);function init(){if(S.value)go()}if(document.readyState=='loading')document.addEventListener('DOMContentLoaded',init);else init()})();</script>''')
_gbody=(f'<p class="lead">Every plain-English guide and free tool on the site, grouped by nation. Each one links to its official sources.</p>'+GCPICK
 +f'<p class="small">Jump to: '+' · '.join(f'<a href="#g-{re.sub(r"[^a-z]+","-",nm.lower()).strip("-")}">{e(nm)}</a>' for nm,*_ in GHUB)+'</p>'
 +_gb+'<h2>More</h2><ul><li><a href="councils.html">All councils with local rules</a></li><li><a href="changes.html">Latest rule changes</a></li><li><a href="newsletter.html">Weekly "what changed" email</a></li></ul>'
 +'<p class="small">General information only, not legal or tax advice. The UK Short-Let Rules team</p>')
page(_gf,_gt,_gbody,desc=_gd,full_title=_gt+' | UK Short-Let Rules Tracker',head=OGT(_gf,_gt,_gd)+f'<script type="application/ld+json">{_gld}</script>')
