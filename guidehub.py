# ---- Guides hub (/guides): every guide and free tool, grouped by nation. Titles = each page's H1, descriptions = its own meta description ----
import html as _H
def _gmeta(fn):
    t=open(fn).read()
    h=re.search(r'<h1>(.*?)</h1>',t,re.S);m=re.search(r'<meta name="description" content="([^"]*)">',t)
    return _H.unescape(re.sub(r'<[^>]+>','',h.group(1)).strip()),(GLONG.get(fn) or _H.unescape(m.group(1)))  # GLONG: card keeps the long description when GMETA shortens the meta one
GHUB=[('England',['england-short-term-let-rules-2027.html','england-holiday-let-planning-permission.html','england-second-homes-council-tax-premium.html','holiday-let-fire-safety-england.html'],['london-90-night-counter.html','london-second-homes-council-tax-premium.html'],'england.html'),
 ('Wales',['wales-second-homes-council-tax-premium.html','holiday-let-fire-safety-wales.html','wales-visitor-accommodation-licensing.html'],['wales-registration-checker.html'],'wales.html'),
 ('Scotland',['scotland-short-term-let-licence-guide.html','short-term-let-fire-safety-scotland.html'],['scotland-short-term-let-licence-fees.html','scotland-licence-renewal-checker.html','scotland-business-rates-checker.html'],'scotland.html'),
 ('Northern Ireland',['northern-ireland-tourism-certificate-guide.html'],[],'northern-ireland.html'),
 ('UK-wide',['holiday-let-tax-after-fhl-abolition.html','holiday-let-insurance-uk.html'],['checker.html','short-let-planning-permission-by-council.html','second-homes-council-tax-premium-by-council.html','uk-visitor-levy-map.html','levy-calculator.html','uk-levy-and-licence-deadlines.html','occupancy-threshold-tracker.html','buyer-due-diligence-checker.html','deadlines.html','consultations.html'],None)]
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
def RCPICK(p,cta,pcta,ev,h2,intro,ch=None,hide='section.alertcta'):
    """Shared 'Rules in your council' picker (used by /guides and /changes). p = id prefix, cta = alert form data-cta, pcta = council-page link data-cta,
    ev = GA4 event name (once per distinct pick per page view), ch = optional {('c',slug)|('n',nation_id): [change lines]} shown as 'Latest logged changes',
    hide = CSS selector of the generic alert boxes hidden while the result box shows (restored when the placeholder is chosen)."""
    D={'c':{},'n':{}};O=''
    for _n in d['nations']:
        cs=sorted([c for c in d['councils'] if c['nation']==_n['name'] and c['verified'] and _sl(c) not in PICK_EXCL and _sl(c) in _gcx],key=lambda c:c['name'].replace('City of ',''))
        D['n'][_n['id']]={'n':_n['name'],'r':_n['summary'],'u':_n['id']}
        if ch is not None:D['n'][_n['id']]['ch']=ch.get(('n',_n['id']),[])
        O+=f'<optgroup label="{e(_n["name"])}"><option value="nation:{_n["id"]}">All of {e(_n["name"])}</option>'+''.join(f'<option value="council:{_sl(c)}">{e(c["name"])}</option>' for c in cs)+'</optgroup>'
        for c in cs:
            D['c'][_sl(c)]={'n':c['name'],'r':c['rule'],'src':c['source'],'nx':_gcx[_sl(c)]['nx']}
            if ch is not None:D['c'][_sl(c)]['ch']=ch.get(('c',_sl(c)),[])
    assert not any('kinross' in k for k in D['c']) and 'kinross' not in O.lower()
    J=json.dumps(D,ensure_ascii=False).replace('</','<\\/')
    chh=(f'<h4 class="rcch">Latest logged changes</h4><ul class="anx" id="{p}-ch"></ul>' if ch is not None else '')
    sid='g-council' if p=='gc' else p+'-council'
    return (f'<section class="box ghpick" id="{sid}" aria-labelledby="{p}-h"><h2 id="{p}-h">{h2}</h2><p>{intro}</p>'
     f'<label for="{p}-sel"><b>Your council</b></label><select id="{p}-sel"><option value="">Choose your council</option>'+O+'</select>'
     f'<div id="{p}-res" class="ghres" hidden><h3 id="{p}-n"></h3><p id="{p}-r"></p>{chh}<p class="small"><a id="{p}-l" href="councils.html" data-cta="{pcta}">Full rules</a><span id="{p}-sw"> · <a id="{p}-s" href="councils.html" rel="nofollow">Official source</a></span></p></div>'
     '<p class="small">Not listed? <a href="councils.html">Browse all councils</a>.</p></section>'
     f'<div class="alertbox" id="{p}-alert" hidden><h2>Get an email when short-let rules change in <span id="{p}-an">your council</span></h2><p id="{p}-why">We track these rules against official sources and email you when one of them changes.</p><p class="anxh" id="{p}-nxh" hidden><b>Dates we\'re watching:</b></p><ul class="anx" id="{p}-nx" hidden></ul><p class="small">Plus one short weekly UK "what changed" email. Free. Unsubscribe any time.</p>'
     +FORMX.replace('<form class="signup"',f'<form class="signup" id="{p}-form" data-cta="{cta}" data-area="" data-area-name=""',1).replace('>Subscribe<','>Get free alerts<')+'</div>'
     '<script>(function(){var P="'+p+'",H="'+hide+'",EV="'+ev+'",D='+J+_RCJS)
_RCJS=r''',S=$('sel'),R=$('res'),A=$('alert'),F=$('form'),seen={};
function $(i){return document.getElementById(P+'-'+i)}
function sw(h){[].forEach.call(document.querySelectorAll(H),function(W){W.hidden=h})}
function go(ev){var v=S.value,m=v.match(/^(council|nation):(.+)$/),x=m&&(m[1]=='council'?D.c[m[2]]:D.n[m[2]]);
if(!x){R.hidden=true;A.hidden=true;sw(false);return}
var c=m[1]=='council';$('n').textContent=c?x.n:'All of '+x.n;$('r').textContent=x.r;var L=$('l');L.href=c?'councils/'+m[2]:x.u;L.textContent=c?'Full '+x.n+' rules':'All '+x.n+' rules';
if(c&&x.src){$('s').href=x.src;$('sw').hidden=false}else $('sw').hidden=true;
var CH=$('ch');if(CH){CH.innerHTML='';(x.ch&&x.ch.length?x.ch:['No change logged yet for '+(c?x.n:'all of '+x.n)+'. We check its rules against official sources.']).forEach(function(t){var li=document.createElement('li');li.textContent=t;CH.appendChild(li)})}
R.hidden=false;
if(F.getAttribute('data-area')!=v){var M=F.querySelector('.msg');if(M)M.textContent=''}F.setAttribute('data-area',v);F.setAttribute('data-area-name',x.n);$('an').textContent=c?x.n:'all of '+x.n;
$('why').textContent=c?'We track licensing, planning, visitor levy and fee rules for '+x.n+' against official sources, and email you when one of them changes.':'We track the '+x.n+' rules against official sources and email you when one of them changes.';
var NX=$('nx'),L2=c&&x.nx?x.nx:[];NX.innerHTML='';L2.forEach(function(t){var li=document.createElement('li');li.textContent=t;NX.appendChild(li)});NX.hidden=$('nxh').hidden=!L2.length;
A.hidden=false;sw(true);if(ev&&!seen[v]){seen[v]=1;try{gtag('event',EV,{area_type:m[1],council:m[2]})}catch(e){}}}
S.addEventListener('change',go);function init(){if(S.value)go()}if(document.readyState=='loading')document.addEventListener('DOMContentLoaded',init);else init()})();</script>'''
# /guides: 'Rules in your council' block (growth push, 2 Nov): pick a council (council:<slug>) or a whole nation (nation:<id>) -> that area's one-line rule summary
# (data.json 'rule' / nation 'summary', already shown on /councils and the nation pages, with the council's official source), a link to its page,
# its next sourced key dates, and an in-context alert box pre-set to the pick (data-cta guides-council-result). Hides the sitewide box while shown.
# Perth & Kinross (PICK_EXCL) never appears. GA4: guides_council_pick {area_type, council}, once per distinct pick per page view.
GCPICK=RCPICK('gc','guides-council-result','guides-council-page','guides_council_pick','Rules in your council','Pick your council, or a whole nation, to see its short-let rules in brief, with a link to its full page and free alerts when they change.')
_gbody=(f'<p class="lead">Every plain-English guide and free tool on the site, grouped by nation. Each one links to its official sources.</p>'+GCPICK
 +f'<p class="small">Jump to: '+' · '.join(f'<a href="#g-{re.sub(r"[^a-z]+","-",nm.lower()).strip("-")}">{e(nm)}</a>' for nm,*_ in GHUB)+'</p>'
 +_gb+'<h2>More</h2><ul><li><a href="councils.html">All councils with local rules</a></li><li><a href="changes.html">Latest rule changes</a></li><li><a href="newsletter.html">Weekly "what changed" email</a></li></ul>'
 +'<p class="small">General information only, not legal or tax advice. The UK Short-Let Rules team</p>')
page(_gf,_gt,_gbody,desc=_gd,full_title=_gt+' | UK Short-Let Rules Tracker',head=OGT(_gf,_gt,_gd)+f'<script type="application/ld+json">{_gld}</script>')
