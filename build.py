import json,html
d=json.load(open('data.json'));e=html.escape;C=d['checked']
import re,os
SITE='https://ukshortletrules.co.uk/';PAGES=[]
def mknav(p):return f'<nav><a href="{p}index.html">Home</a>'+''.join(f'<a href="{p}{n["id"]}.html">{n["name"]}</a>' for n in d['nations'])+f'<a href="{p}councils.html">Councils</a><a href="{p}changes.html">Changes</a><a href="{p}uk-visitor-levy-map.html">Levy map</a><a href="{p}scotland-short-term-let-licence-guide.html">Scot licence guide</a><a href="{p}scotland-business-rates-checker.html">Scot rates checker</a><a href="{p}wales-registration-checker.html">Wales checker</a><a href="{p}newsletter.html">Newsletter</a></nav>'
def page(f,t,b,desc=None,full_title=None,head=''):
    p='../'*f.count('/');nav=mknav(p);PAGES.append(f)
    if p:b=b.replace('src="signup.js"',f'src="{p}signup.js"')
    desc=desc or f'{t}: licensing, planning, tax and levy rules for UK short-term and holiday lets, with official sources.'
    os.makedirs(os.path.dirname(f) or '.',exist_ok=True)
    open(f,'w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(full_title or t+' | UK Short-Let Rules Tracker')}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{SITE}{f}"><link rel="stylesheet" href="{p}style.css">{head}</head><body><header><a class="brand" href="{p}index.html">UK Short-Let Rules Tracker</a>{nav}</header><main><h1>{e(t)}</h1>{b}</main><footer>Last checked {C}. General information only, not legal or tax advice. Always check the linked official source.<br><span class="small">Want to reach UK hosts? <a href="{p}sponsor.html">Sponsor the tracker</a></span></footer></body></html>''')
FORM='''<form class="signup" data-endpoint="%s"><input type="email" name="email" placeholder="you@example.com" required aria-label="Email"><input type="text" name="website" class="hp" tabindex="-1" autocomplete="off"><button>Subscribe</button><p class="msg small"></p></form><script src="signup.js"></script>''' % e(d.get('newsletter_endpoint',''))
src=lambda s:' '.join(f'<a href="{e(u)}" rel="nofollow">source</a>' for u in s) or '<em>no source yet</em>'
cards=''.join(f'<a class="card" href="{n["id"]}.html"><h2>{n["name"]}</h2><p>{e(n["summary"])}</p></a>' for n in d['nations'])
latest=''.join(f'<li><b>{c["date"]}</b> [{c["nation"]}] {e(c["text"])}</li>' for c in d['changes'][:4])
page('index.html','Current short-let rules across the UK',f'<p class="lead">Licensing, planning, tax and safety rules for UK holiday-let and short-term-let hosts, with links to official sources.</p><div class="grid">{cards}</div><h2>Free tools</h2><ul><li><a href="wales-registration-checker.html">Wales: do I need to register with the WRA?</a> (4-question checker)</li><li><a href="scotland-business-rates-checker.html">Scotland: business rates or council tax?</a> (140/70 nights checker)</li><li><a href="scotland-short-term-let-licence-guide.html">Scotland: how to get a short-term let licence</a> (steps and checklist)</li><li><a href="uk-visitor-levy-map.html">UK visitor levy and tourist tax map</a></li></ul><h2>Latest changes</h2><ul>{latest}</ul><p><a href="changes.html">Full changes log</a></p><div class="box"><h2>Weekly "what changed" email</h2><p>One short, sourced email a week. Unsubscribe any time.</p>'+FORM+'</div>')
for n in d['nations']:
    rows=''.join(f'<tr><td>{e(r["topic"])}</td><td><span class="tag{" warn" if "UNVERIFIED" in r["status"] else ""}">{e(r["status"])}</span></td><td>{e(r["text"])}</td><td>{src(r["sources"])}</td></tr>' for r in n['rules'])
    page(n['id']+'.html',n['name'],f'<p class="lead">{e(n["summary"])}</p>'+('<p class="box"><b>New:</b> <a href="wales-registration-checker.html">Do I need to register with the WRA? Take the 4-question checker</a></p>' if n['id']=='wales' else '<p class="box"><b>New:</b> <a href="scotland-short-term-let-licence-guide.html">How to get a short-term let licence: steps and a tick-off checklist</a></p>' if n['id']=='scotland' else '')+f'<div class="tw"><table><tr><th>Topic</th><th>Status</th><th>Rule</th><th>Official source</th></tr>{rows}</table></div>')
slug=lambda c:c.get('slug') or re.sub(r'[^a-z0-9]+','-',c['name'].lower().replace('&','and')).strip('-')
rows=''.join(f'<tr><td>{f'<a href="councils/{slug(c)}.html">{e(c["name"])}</a>' if c["verified"] else e(c["name"])}</td><td>{c["nation"]}</td><td>{e(c["rule"])}</td><td>{"✔" if c["verified"] else "<span class=\"tag warn\">unverified</span>"}</td><td>{src([c["source"]] if c["source"] else [])}</td></tr>' for c in d['councils'])
page('councils.html','Councils with notable local rules',f'<p>Click a council for its own page with official sources and key dates.</p><div class="tw"><table><tr><th>Council</th><th>Nation</th><th>Rule</th><th>Verified</th><th>Source</th></tr>{rows}</table></div>')
rows=''.join(f'<tr><td>{c["date"]}</td><td>{c["nation"]}</td><td>{e(c["text"])}</td><td>{src([c["source"]])}</td></tr>' for c in d['changes'])
page('changes.html','Changes log',f'<div class="tw"><table><tr><th>Date</th><th>Nation</th><th>Change</th><th>Source</th></tr>{rows}</table></div>')
page('newsletter.html','Weekly "what changed" newsletter','<p>One short email every week: what changed, what\'s coming, and deadlines.</p>'+FORM+'<p class="small">We store only your email address (with our email provider, Resend) to send this newsletter. Unsubscribe link in every email. No spam, no sharing.</p>')
page('sponsor.html','Sponsor the tracker','<p>The UK Short-Let Rules Tracker is a free, independent guide to the rules for UK holiday-let and short-term-let hosts.</p><p>If you would like to sponsor the tracker, or talk about another way of working together, please get in touch: <a href="mailto:hello@ukshortletrules.co.uk">hello@ukshortletrules.co.uk</a>.</p><p>Any sponsorship would be clearly labelled, and sponsors never affect the content.</p>')

# ---- Per-council pages ----
U='<span class="tag warn">UNVERIFIED</span>'
SC_LIC=('Licence needed (Scotland-wide). All short-term lets (secondary letting, home letting, home sharing) need a licence from the council before taking bookings or guests. <a href="../scotland-short-term-let-licence-guide.html">Step-by-step licence guide and checklist</a>.',['https://www.gov.scot/publications/short-term-lets/'])
WA_REG=('No council licence yet. Wales-wide: if you take bookings of 31 nights or fewer you must register with the Welsh Revenue Authority by 31 Mar 2027 (free, applies even with no council levy). A national licensing scheme is legislated but not in force (default commencement March 2030). <a href="../wales-registration-checker.html">Check if you must register</a>.',['https://www.gov.wales/registering-visitor-accommodation-overview','https://industry.visitwales.com/about-us/tourism-policies-and-legislation'])
EN_LIC=('No licensing or registration scheme in force in England.',[])
CX={
'city-of-edinburgh':dict(lic=SC_LIC,ctrl=('Yes: the whole city has been a short-term let control area since 5 Sep 2022. Using a whole dwelling that isn\'t your main home as a short-term let very likely needs planning permission.',['https://www.mygov.scot/short-term-let-licences/planning-permission-control-areas']),
 levy=('5% of the accommodation cost, first 5 consecutive nights, stays from 24 Jul 2026. Quarterly returns via visitorlevy.scot.',['https://www.edinburgh.gov.uk/visitorlevyinformation']),
 fees=('Licence fees: see the council\'s licensing page (not summarised here). Operating without a licence can mean a fine of up to £2,500.',['https://www.edinburgh.gov.uk/licences-permits/licences-permits-applications/10']),
 dates=['5 Sep 2022: control area in force','24 Jul 2026: visitor levy applies to stays']),
'glasgow-city':dict(lic=SC_LIC,ctrl=('No control area in force.',['https://www.mygov.scot/short-term-let-licences/planning-permission-control-areas']),
 levy=('5% from 25 Jan 2027 on the whole stay; liable on bookings made from 1 Apr 2026.',['https://www.glasgow.gov.uk/article/14800/Accommodation-providers']),
 fees=('Licence fees: not summarised here, check the council.',[]),dates=['1 Apr 2026: bookings made from this date are liable','25 Jan 2027: levy starts']),
'highland':dict(lic=SC_LIC,ctrl=('Badenoch & Strathspey ward is a control area (since 4 Mar 2024). Rest of Highland: none.',['https://www.mygov.scot/short-term-let-licences/planning-permission-control-areas']),
 levy=('Proposed only: consultation on a £5 per room per night levy opened 7 Sep 2026; council decision due 10 Dec 2026, then an 18-month lead-in.',['https://www.highland.gov.uk/news/article/17462/highland-council-opens-statutory-public-consultation-on-a-tiered-fixed-amount-visitor-levy-proposal']),
 fees=('Licence fees: not summarised here, check the council.',[]),dates=['4 Mar 2024: Badenoch & Strathspey control area','10 Dec 2026: levy decision due']),
'perth-and-kinross':dict(lic=(SC_LIC[0]+' Public register at pkc.gov.uk/article/22511.',SC_LIC[1]+['https://www.pkc.gov.uk/article/22511']),
 ctrl=('Proposed, not in force: Highland Perthshire and the northern part of Eastern Perthshire, agreed 17 Jun 2026, awaiting Scottish Ministers\' approval. Flats already need planning permission to become a short-term let.',['https://consult.pkc.gov.uk/communities/proposal-of-short-term-let-control-area/']),
 levy=('Draft scheme under statutory consultation since 19 Aug 2026 (12 weeks). No decision yet. Reported rate of £4 per room per night and closing date of 11 Nov 2026: '+U+'.',['https://www.pkc.gov.uk/article/24551/Perth-and-Kinross-Visitor-Levy']),
 fees=('3-year licence, new or renewal (Policy Statement, 10 Mar 2025). Secondary letting: £350 (1–2 guests), £530 (3–6), £900 (7–10), £1,600 (11+). Home letting/sharing: £175 / £265 / £450 / £800. Variation or transfer £75.',['https://www.pkc.gov.uk/media/50153/Short-term-Lets-Policy-Statement/pdf/Short-term_Lets_Licensing_Policy_Statement_-_10_MARCH_2025.pdf?m=1741781506817']),
 dates=['17 Jun 2026: control area proposal agreed (not in force)','19 Aug 2026: levy consultation opened','11 Nov 2026: consultation closing date ('+U+')']),
'greater-london-all-boroughs':dict(lic=EN_LIC,ctrl=('90 nights per calendar year cap on letting a whole home short-term without planning permission.',['https://www.legislation.gov.uk/ukpga/2015/20/section/44']),
 levy=('No visitor levy.',[]),fees=('None.',[]),dates=[]),
'cornwall':dict(lic=EN_LIC,ctrl=('None listed.',[]),levy=('No visitor levy. Council tax: 100% second-home premium from 1 Apr 2025, with exceptions (e.g. holiday-only planning conditions).',['https://www.cornwall.gov.uk/council-tax/second-homes/']),
 fees=('None.',[]),dates=['1 Apr 2025: second-home premium started']),
'gwynedd':dict(lic=WA_REG,ctrl=('Article 4 direction (C3 to C5/C6) was quashed and is not in force; the Court of Appeal refused appeal on 6 Feb 2026.',['https://www.gwynedd.llyw.cymru/en-gb/planning-building-control-and-listed-buildings/planning/article-4-direction']),
 levy=('No levy listed here yet. Check the gov.wales list of councils charging the levy.',['https://www.gov.wales/visitor-levy-wales']),fees=('WRA registration is free.',[]),dates=['6 Feb 2026: appeal refused, Article 4 not in force','31 Mar 2027: WRA registration deadline']),
'pembrokeshire':dict(lic=WA_REG,ctrl=('No control area or Article 4 direction listed here.',[]),
 levy=('No levy listed here. Check the gov.wales list of councils charging the levy.',['https://www.gov.wales/check-if-local-council-charges-visitor-levy-wales']),
 fees=('WRA registration is free. Council tax second-home premium: 125% from 1 Apr 2026, on top of the standard charge (150% in 2025-26, 200% in 2024-25). Exceptions apply.',['https://www.pembrokeshire.gov.uk/council-tax-discounts/second-homes']),
 dates=['1 Apr 2026: second-home premium 125%','31 Mar 2027: WRA registration deadline']),
'cardiff':dict(lic=WA_REG,ctrl=('No Article 4 direction listed.',[]),
 levy=('Visitor levy for new bookings for stays from 1 Apr 2027: £1.30 per person per night (75p for shared hostel/dorm rooms and tent pitches).',['https://www.gov.wales/visitor-levy-wales']),
 fees=('WRA registration is free.',[]),dates=['31 Mar 2027: WRA registration deadline','1 Apr 2027: Cardiff levy starts']),
}
def sec(h,x):return f'<h2>{h}</h2><p>{x[0]}</p>'+(f'<p class="small">Source: {src(x[1])}</p>' if x[1] else '')
made=[];skipped=[]
for c in d['councils']:
    s=slug(c)
    if s not in CX or not c['verified']:skipped.append(c['name']);continue
    x=CX[s];dt=' '.join(reversed(C.split('-')));import datetime;dt=datetime.date.fromisoformat(C).strftime('%-d %b %Y')
    t=f'Short-term let rules in {c["name"]} (updated {dt})'
    kd=''.join(f'<li>{k}</li>' for k in x['dates']) or '<li>None listed.</li>'
    b=f'<p class="lead">{e(c["rule"])}</p>'+sec('Licensing or registration',x['lic'])+sec('Control area / planning',x['ctrl'])+sec('Visitor levy',x['levy'])+sec('Fees',x['fees'])+f'<h2>Key dates</h2><ul>{kd}</ul><p><a href="../{ {"Scotland":"scotland","Wales":"wales","England":"england"}[c["nation"]]}.html">All {c["nation"]} rules</a> · <a href="../councils.html">All councils</a></p><div class="box"><h2>Get told when {e(c["name"])} rules change</h2>'+FORM+'</div>'
    page(f'councils/{s}.html',t,b,desc=f'Short-term let licensing, control area, visitor levy, fees and key dates for {c["name"]}, {c["nation"]}, with official sources. Updated {dt}.',full_title=t)
    made.append(s)
print('council pages',len(made),'skipped',skipped)

# ---- Wales registration checker ----
WS=['https://www.gov.wales/registering-visitor-accommodation-overview','https://www.gov.wales/register-your-visitor-accommodation-wales','https://www.gov.wales/failing-register-update-details-or-deregister-your-visitor-accommodation','https://www.gov.wales/visitor-levy-for-visitor-accommodation-providers-overview']
Q=[('q1','Is the accommodation in Wales?','It can be a cottage, flat, lodge, your main home or spare room, B&amp;B, caravan, glamping pod, hostel or pitch.'),
   ('q2','Do you take bookings for overnight stays there?','Even once a year counts (for example, letting your home on Airbnb for a local event). Friends or family staying for free do not count.'),
   ('q3','Are any of those bookings for 31 nights or fewer?','One short booking is enough.'),
   ('q4','Are you responsible for the accommodation (for example, you own or rent it)?','If an agent or management company runs it for you, you are still the one who must register (they can do it on your behalf).')]
qs=''.join(f'<fieldset class="box q" id="{i}"><legend><b>{n+1}. {q}</b></legend><p class="small">{h}</p><label><input type="radio" name="{i}" value="y"> Yes</label> <label><input type="radio" name="{i}" value="n"> No</label></fieldset>' for n,(i,q,h) in enumerate(Q))
b=f'''<p class="lead">Answer {len(Q)} quick questions to see if you must register your visitor accommodation with the Welsh Revenue Authority (WRA).</p>{qs}
<div id="result" class="box" hidden aria-live="polite"><h2 id="rh"></h2><div id="rt"></div><h3>Get told when this changes</h3><p>One short, sourced email a week when Wales (or UK) short-let rules change.</p>{FORM}<p class="small"><b>Not legal advice.</b> This is general information based on the official guidance below. Always check the official source or contact the WRA.</p></div>
<h2>Official sources</h2><ul>{"".join(f'<li><a href="{u}" rel="nofollow">{u}</a></li>' for u in WS)}</ul>
<script>
(function(){{var ids=['q1','q2','q3','q4'];var R=document.getElementById('result'),H=document.getElementById('rh'),T=document.getElementById('rt');
var reg='<p><a href="https://www.gov.wales/register-your-visitor-accommodation-wales">Register with the WRA online</a>.</p>';
var no={{q1:'Registration is only for visitor accommodation in Wales. Check the rules for <a href="scotland.html">Scotland</a>, <a href="england.html">England</a> or <a href="northern-ireland.html">Northern Ireland</a>.',
q2:'You do not have to register if you do not take bookings (for example friends or family staying for free) or no longer take bookings for overnight stays. If you start taking bookings, you will need to register.',
q3:'Registration applies to bookings of 31 nights or less. If every booking you take is longer than 31 nights, you do not have to register. If you ever take a shorter booking, you will.',
q4:'The provider responsible for the accommodation (for example the owner or the person renting it) must register. If that is not you, the responsible person must register. Agents can register on their behalf.'}};
function upd(){{for(var i=0;i<ids.length;i++){{var el=document.getElementById(ids[i]);el.hidden=false;var v=(document.querySelector('input[name='+ids[i]+']:checked')||{{}}).value;
if(!v){{for(var j=i+1;j<ids.length;j++)document.getElementById(ids[j]).hidden=true;R.hidden=true;return;}}
if(v==='n'){{for(var j=i+1;j<ids.length;j++)document.getElementById(ids[j]).hidden=true;H.textContent='You probably do not need to register';T.innerHTML='<p>'+no[ids[i]]+'</p>';R.hidden=false;return;}}}}
H.textContent='You must register with the Welsh Revenue Authority by 31 March 2027';
T.innerHTML='<ul><li><b>It is free.</b></li><li>It is required by law <b>even if your local council does not charge a Visitor Levy</b>.</li><li>Include all premises in one registration if the same people are responsible for each.</li><li>You get a unique registration number; some details appear on a public register.</li><li>Update your details within 30 days if anything changes.</li><li>If you do not register by 31 March 2027 you may have to pay a penalty.</li></ul>'+reg;R.hidden=false;}}
document.querySelectorAll('.q input').forEach(function(x){{x.addEventListener('change',upd);}});upd();}})();
</script>'''
page('wales-registration-checker.html','Do I need to register my holiday let in Wales?',b,desc='Free 4-question checker: do you need to register your Wales holiday let or short-term let with the Welsh Revenue Authority by 31 March 2027? Plain English, official sources.',full_title='Wales visitor accommodation registration checker (WRA, 31 Mar 2027) | UK Short-Let Rules Tracker')

exec(open('tools_extra.py').read())
exec(open('guides.py').read())

# ---- sitemap / robots ----
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE}{"" if f=="index.html" else f}</loc><lastmod>{C}</lastmod></url>\n' for f in PAGES)+'</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
