# ---- Checker v2: "Does my let need a licence or registration?" nation -> council -> type of let ----
# Uses only facts already on the site (data.json nation rules + CX council sections). No new rules.
from urllib.parse import urlparse as _up
_SN={'www.gov.scot':'Scottish Government (gov.scot)','www.mygov.scot':'mygov.scot','www.gov.uk':'GOV.UK','www.legislation.gov.uk':'legislation.gov.uk','www.gov.wales':'GOV.WALES','industry.visitwales.com':'Visit Wales (industry site)','www.tourismni.com':'Tourism NI','www.finance-ni.gov.uk':'Department of Finance NI'}
def _sname(u):
    h=_up(u).netloc.lower();return _SN.get(h,h[4:] if h.startswith('www.') else h)
def _srcs(L):
    out=[]
    for u in L:
        n=_sname(u)
        if n not in out:out.append(n)
    return out
TYPES=[('whole',"A whole home that isn't my main home (holiday let or second home)"),('away',"My own home, let while I'm away"),('room',"A room or rooms in my home, while I live there")]
_tx2=lambda v:_tx(re.sub(r'\s*<a [^>]*>[^<]*</a>\.?','',v))
_R={n['id']:{r['topic']:r for r in n['rules']} for n in d['nations']}
V2={'scotland':{'h':'Yes: you need a short-term let licence from {C}.',
  'p':['All short-term lets in Scotland (secondary letting, home letting and home sharing) need a licence from the local council before you take bookings or receive guests. Operating without a licence is a criminal offence.'],
  'kind':{'whole':'In the licence rules, this kind of let is called secondary letting.','away':'In the licence rules, this kind of let is called home letting.','room':'In the licence rules, this kind of let is called home sharing.'},
  'extra':{'whole':['Planning: Scotland has two short-term let control areas in force, the whole City of Edinburgh and Badenoch & Strathspey ward in Highland. In a control area, using a whole dwelling that isn\'t your main home as a short-term let very likely needs planning permission.'],
           'away':['Planning: the control-area planning rule is about using a whole dwelling that isn\'t your main home.'],
           'room':['Planning: the control-area planning rule is about using a whole dwelling that isn\'t your main home.']},
  'src':_srcs(_R['scotland']['Licensing']['sources'][:1]+_R['scotland']['Planning / control areas']['sources'][:1])},
 'england':{'h':'No licence or registration needed yet.',
  'p':['England has no licensing or registration scheme for short-term lets in force. GOV.UK says a national registration scheme is expected to begin in March 2027. No regulations, portal or fee have been published yet.'],
  'kind':{},
  'extra':{'whole':['Planning: your local planning authority decides whether your letting is a material change of use, and councils can use Article 4 directions. The proposed C5 short-term let use class is not law.'],'away':[],'room':[]},
  'london':{'whole':'London: in Greater London, a whole home can be short-let for up to 90 nights per calendar year without planning permission. Going over that needs permission (Deregulation Act 2015, s.44).','away':'London: in Greater London, a whole home can be short-let for up to 90 nights per calendar year without planning permission. Going over that needs permission (Deregulation Act 2015, s.44).','room':'London: the 90-night rule is about letting a whole home short-term.'},
  'src':_srcs(_R['england']['Registration scheme']['sources'][:1])},
 'wales':{'h':'Yes: you must register with the Welsh Revenue Authority (free). No licence yet.',
  'p':['From 1 Oct 2026, anyone taking bookings of 31 nights or less must register with the Welsh Revenue Authority by 31 Mar 2027. Registration is free and applies even where no visitor levy exists.','Licensing: a licensing scheme for self-contained self-catering lets has Royal Assent but is not in force. Its legal default start is March 2030, with consultation on regulations first.'],
  'kind':{},'extra':{'whole':[],'away':[],'room':[]},
  'src':_srcs(_R['wales']['Registration (WRA)']['sources'][:1]+_R['wales']['Licensing']['sources'][:1])},
 'northern-ireland':{'h':'Yes: you need a Tourism NI certificate.',
  'p':['Under the Tourism (NI) Order 1992, all visitor accommodation in Northern Ireland needs a current Tourism NI certificate after an inspection. Certificates last 4 years.'],
  'kind':{},'extra':{'whole':[],'away':[],'room':[]},
  'src':_srcs(_R['northern-ireland']['Certification']['sources'][:2])}}
V2D={'types':TYPES,'nations':[],'councils':[]}
for n in d['nations']:
    V2D['nations'].append(dict(V2[n['id']],id=n['id'],name=n['name'],url=n['id']+'.html'))
for c in d['councils']:
    s=slug(c)
    if s in CX and c['verified']:
        x=CX[s];V2D['councils'].append({'n':c['name'],'nat':NAT[c['nation']],'s':s,'ldn':s=='greater-london-all-boroughs',
          'sec':[[h,_tx2(x[k][0]),_srcs(x[k][1])] for h,k in (('Licensing or registration','lic'),('Planning','ctrl')) if _tx2(x[k][0]) and _tx2(x[k][0])!='None listed.'],'nx':[_tx(k) for k in NEXTD(x['dates'])]})
V2J=json.dumps(V2D,ensure_ascii=False).replace('</','<\\/')
V2F='''<form class="ck2" onsubmit="return false"><fieldset><legend>1. Where is the let?</legend><label for="v2-n" class="sr">Nation</label><select id="v2-n"><option value="">Choose a nation</option></select></fieldset>
<fieldset id="v2-cf" hidden><legend>2. Which council?</legend><label for="v2-c" class="sr">Council</label><select id="v2-c"></select></fieldset>
<fieldset id="v2-tf" hidden><legend>3. What type of let is it?</legend><div id="v2-t"></div></fieldset></form>
<div id="v2-out" aria-live="polite"></div>
<div class="alertbox" id="v2-alert" hidden><h2>Get an email when short-let rules change in <span id="v2-an">your council</span></h2><p id="v2-why">We track these rules against official sources and email you when one of them changes.</p><p class="anxh" id="v2-nxh" hidden><b>Dates we're watching:</b></p><ul class="anx" id="v2-nx" hidden></ul><p class="small">Plus one short weekly UK "what changed" email. Free. Unsubscribe any time.</p>'''+FORMX.replace('<form class="signup"','<form class="signup" id="v2-form" data-cta="checker-v2" data-area="" data-area-name=""',1).replace('>Subscribe<','>Get free alerts<')+'</div>'
V2JS='''<script>(function(){var D=%s,N=document.getElementById('v2-n'),C=document.getElementById('v2-c'),CF=document.getElementById('v2-cf'),TF=document.getElementById('v2-tf'),T=document.getElementById('v2-t'),O=document.getElementById('v2-out'),A=document.getElementById('v2-alert'),AN=document.getElementById('v2-an'),F=document.getElementById('v2-form');
function el(t,x,c){var e=document.createElement(t);if(x)e.textContent=x;if(c)e.className=c;return e}
D.nations.forEach(function(n){var o=el('option',n.name);o.value=n.id;N.appendChild(o)});
D.types.forEach(function(t,i){var l=el('label','','v2-ty'),r=document.createElement('input');r.type='radio';r.name='v2t';r.value=t[0];r.addEventListener('change',show);l.appendChild(r);l.appendChild(document.createTextNode(' '+t[1]));T.appendChild(l)});
function nat(){return D.nations.filter(function(x){return x.id===N.value})[0]}
function cou(){return D.councils.filter(function(x){return x.s===C.value})[0]}
function typ(){var r=T.querySelector('input:checked');return r?r.value:''}
function show(){O.innerHTML='';A.hidden=true;var S0=document.querySelector('section.alertcta');if(S0)S0.hidden=false;var n=nat(),t=typ();if(!n||!t||(!CF.hidden&&C.value===''))return;var c=cou(),cn=c?c.n:'your council';
var b=el('div','','ck-res v2-res');b.appendChild(el('h2',n.h.replace('{C}',cn)));n.p.forEach(function(x){b.appendChild(el('p',x))});if(n.kind[t])b.appendChild(el('p',n.kind[t]));
(n.extra[t]||[]).forEach(function(x){b.appendChild(el('p',x))});
if(n.london&&(c?c.ldn:true)){b.appendChild(el('p',(c?'':'If the let is in Greater London: ')+n.london[t]))}
b.appendChild(el('p','Official source: '+n.src.join('; ')+'.','small src'));
if(c&&c.sec.length){b.appendChild(el('h3','What our '+c.n+' page says'));c.sec.forEach(function(s){var d=el('div');d.appendChild(el('h4',s[0]));d.appendChild(el('p',s[1]));if(s[2].length)d.appendChild(el('p','Official source: '+s[2].join('; ')+'.','small src'));b.appendChild(d)})}
var m=el('p','','ck-more'),a=el('a',c?'See everything for '+c.n+': licensing, planning, levy and fees':'See all the '+n.name+' rules');a.href=c?'councils/'+c.s:n.url.replace('.html','');m.appendChild(a);b.appendChild(m);
b.appendChild(el('p','General information only, not legal or tax advice. Always check the official source.','small'));O.appendChild(b);
F.setAttribute('data-area',c?'council:'+c.s:'nation:'+n.id);F.setAttribute('data-area-name',c?c.n:n.name);AN.textContent=c?c.n:'all of '+n.name;var W=document.getElementById('v2-why'),NH=document.getElementById('v2-nxh'),NX=document.getElementById('v2-nx');W.textContent=c?'We track licensing, planning, visitor levy and fee rules for '+c.n+' against official sources, and email you when one of them changes.':'We track the '+n.name+' rules against official sources and email you when one of them changes.';NX.innerHTML='';var L2=c&&c.nx?c.nx:[];L2.forEach(function(x){NX.appendChild(el('li',x))});NX.hidden=NH.hidden=!L2.length;A.hidden=false;var S=document.querySelector('section.alertcta');if(S)S.hidden=true;}
N.addEventListener('change',function(){var n=nat();C.innerHTML='';var L=n?D.councils.filter(function(x){return x.nat===n.id}):[];
var z=el('option','Choose your council');z.value='';C.appendChild(z);L.forEach(function(x){var o=el('option',x.n);o.value=x.s;C.appendChild(o)});
CF.hidden=!L.length;TF.hidden=!n;show()});
C.addEventListener('change',show);})();</script>'''
V2CSS='<style>.ck2 fieldset{border:0;padding:0;margin:0 0 1rem}.ck2 legend{font-weight:700;font-size:1.1rem;margin-bottom:.4rem}.ck2 select{padding:.6rem;font-size:1rem;width:100%;max-width:28rem}.v2-ty{display:block;padding:.6rem .7rem;margin:.3rem 0;border:1px solid #ccd;border-radius:8px;background:#fff;cursor:pointer;max-width:34rem}.v2-ty input{margin-right:.4rem}.v2-res h2{margin-top:.4rem}.v2-res h4{margin:.8rem 0 .2rem}.v2-res p{margin:.3rem 0}.v2-res .src{color:#445}.ck-more a{font-weight:700}</style>'
page('checker.html','Does my let need a licence or registration?',f'<p class="lead">Answer three quick questions: where your let is, which council, and what type of let it is. You get a plain-English answer, the official source to check, and a link to your council page.</p><div class="box">{V2F[:V2F.index("<div id=\"v2-out\"")]}</div>{V2F[V2F.index("<div id=\"v2-out\""):]}{V2JS % V2J}<p class="small">Covered councils: {len(V2D["councils"])}. <a href="councils.html">See all council pages</a>. Want a checker on your own site? <a href="embed.html">Get the free embed code</a>.</p>',desc='Free checker: does your UK short-term or holiday let need a licence or registration? Pick your nation, council and type of let for a plain-English answer with the official source.',full_title='Does my short let need a licence or registration? Free checker | UK Short-Let Rules',head=V2CSS)
