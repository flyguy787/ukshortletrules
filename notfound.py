# ---- Custom 404 page (growth push, 5 Nov 2026): GitHub Pages serves /404.html for any missing URL (until now its generic grey page, no way back) ----
# Mistyped or guessed URLs (e.g. /councils/edinburgh, /cornwall, old links in shares or emails) now get: a "Did you mean" link worked out in the browser
# from the missing path (fuzzy match against every council page and every guide/tool), the shared RCPICK 'Rules in your council' picker
# (pre-selected to the matched council when the match is strong, so the in-context alert box is already set to it: data-cta notfound-result),
# popular pages, and the sitewide alert box. noindex, no canonical, not in the sitemap. Every URL is root-absolute because GitHub Pages serves this
# file at any depth. Perth & Kinross (PICK_EXCL) is never suggested. GA4: page_not_found {page_path, suggested}. No new facts.
# exec'd from build.py after the clean-URL pass (so it is not in PAGES / sitemap / lastmod).
_nfc=[c for c in d['councils'] if c['verified'] and _sl(c) not in PICK_EXCL and os.path.exists('councils/'+_sl(c)+'.html')]
_nfi=[{'u':'/councils/'+_sl(c),'n':c['name'],'k':_sl(c)} for c in _nfc]
for _nm,_G,_T,_nf in GHUB:
    for _fn in _G+_T:_nfi.append({'u':'/'+_fn[:-5],'n':_gmeta(_fn)[0],'k':_fn[:-5]})
    if _nf:_nfi.append({'u':'/'+_nf[:-5],'n':_nm+' short-let rules','k':_nf[:-5]})
for _fn,_nm in (('councils','All councils'),('changes','Latest rule changes'),('guides','Guides and free tools'),('newsletter','Weekly "what changed" email')):_nfi.append({'u':'/'+_fn,'n':_nm,'k':_fn})
assert not any('kinross' in (x['u']+x['n']).lower() for x in _nfi)
_NFJ=json.dumps(_nfi,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
NFPICK=RCPICK('nf','notfound-result','notfound-page','notfound_pick','Find your council\'s rules','Pick your council, or a whole nation, to see its short-let rules in brief, with a link to its full page and free alerts when they change.')
NFPICK=NFPICK.replace("L.href=c?'councils/'+m[2]:x.u","L.href=c?'/councils/'+m[2]:'/'+x.u",1)
assert "'/councils/'+m[2]" in NFPICK
_nfpop=[('checker.html','Short-let rules checker','what applies to your let, by council'),('councils.html','All councils','rules council by council, each with its official source'),
 ('second-homes-council-tax-premium-by-council.html','Second homes council tax premium by council','England and Wales table'),('uk-visitor-levy-map.html','UK visitor levy map','where a levy applies or is planned'),
 ('deadlines.html','Deadlines','closing dates, levy start dates and tax deadlines'),('changes.html','Latest rule changes','newest first, each with an official source'),('guides.html','Guides and free tools','everything, grouped by nation')]
_nfbody=('<p class="lead">Sorry, there is no page at <code id="nf-path" style="word-break:break-all">this address</code>. It may have been mistyped, or the link may be out of date.</p>'
 '<div class="answer" id="nf-sugg" hidden><h2>Did you mean <a id="nf-sl" href="/councils" data-cta="notfound-suggest">this page</a>?</h2><p id="nf-sm" class="small">Closest match to the address you typed.</p></div>'
 +NFPICK
 +'<h2>Popular pages</h2><ul>'+''.join(f'<li><a href="{u}"><b>{e(t)}</b></a>: {e(s)}</li>' for u,t,s in _nfpop)+'</ul>'
 +'<p class="small">Followed a broken link from our site? Tell us at hello@ukshortletrules.co.uk and we\'ll fix it. The UK Short-Let Rules team</p>'
 +'<script>(function(){var I='+_NFJ+r''';
var raw=location.pathname,pe=document.getElementById('nf-path');try{raw=decodeURIComponent(raw)}catch(e){}if(pe)pe.textContent=raw;
var seg=raw.toLowerCase().replace(/\.html?$/,'').replace(/\/+$/,'').split('/').pop().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
var STOP={city:1,of:1,and:1,the:1,council:1,county:1,borough:1,district:1,html:1,uk:1,rules:1,short:1,let:1,lets:1,term:1,holiday:1,page:1,councils:1};
function tk(s){return s.split('-').filter(function(w){return w.length>1&&!STOP[w]})}
function lv(a,b){var p=[],i,j,c,q;for(j=0;j<=b.length;j++)p[j]=j;for(i=1;i<=a.length;i++){q=[i];for(j=1;j<=b.length;j++){c=a[i-1]==b[j-1]?0:1;q[j]=Math.min(p[j]+1,q[j-1]+1,p[j-1]+c)}p=q}return p[b.length]}
function tm(w,kt){return kt.some(function(k){return k==w||(w.length>=5&&k.length>=5&&lv(w,k)<=(w.length>=8?2:1))})}
var st=tk(seg),best=null,bs=0;
if(seg.length>=3)I.forEach(function(x){var k=x.k,s=0;if(k==seg)s=1;else if(seg.length>=4&&(k.indexOf(seg)>=0||seg.indexOf(k)>=0))s=.9;else{var kt=tk(k),h=0;st.forEach(function(w){if(tm(w,kt))h++});var u=st.length+kt.length-h;s=u?h/u:0}
if(s>bs){bs=s;best=x}});
var sug=best&&bs>=.5?best:null;
if(sug){var a=document.getElementById('nf-sl');a.href=sug.u;a.textContent=sug.n;document.getElementById('nf-sugg').hidden=false;
var m=sug.u.match(/^\/councils\/([a-z0-9-]+)$/),S=document.getElementById('nf-sel');
if(m&&bs>=.75&&S&&S.querySelector('option[value="council:'+m[1]+'"]')){var go=function(){S.value='council:'+m[1];S.dispatchEvent(new Event('change'))};if(document.readyState=='loading')document.addEventListener('DOMContentLoaded',go);else go()}}
try{gtag('event','page_not_found',{page_path:location.pathname,suggested:sug?sug.u:''})}catch(e){}})();</script>''')
FB_SKIP.add('404.html')
_NFH='<meta name="robots" content="noindex">'
page('404.html','Page not found',_nfbody,desc='This page does not exist. Find your council\'s short-let rules or browse the guides.',full_title='Page not found | UK Short-Let Rules Tracker',head=_NFH)
if '404.html' in PAGES:PAGES.remove('404.html')
_t=_clean_esc(_clean(open('404.html').read()))
_t=re.sub(r'<link rel="canonical" href="[^"]*">','',_t,count=1)
_t=re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "BreadcrumbList".*?</script>','',_t,count=1,flags=re.S)
def _nfabs(m):
    a,q,u=m.group(1),m.group(2),m.group(3)
    if re.match(r'(?:[a-z]+:|//|#|/)',u):return m.group(0)
    u='/' if u in ('./','') else '/'+u
    return f'{a}={q}{u}{q}'
_t=re.sub(r'\b(href|src)=(["\'])([^"\']*)\2',_nfabs,_t)
assert 'rel="canonical"' not in _t and 'BreadcrumbList' not in _t and '.html"' not in _t and 'kinross' not in _t.lower()
assert not re.search(r'\b(?:href|src)="(?![a-z]+:|/|#)',_t),'relative URL left in 404.html'
open('404.html','w').write(_t)
