# ---- Guide: Scotland short-term let licence step by step + checklist ----
import json as _j
GS=[('mygov.scot: Getting a short-term let licence','https://www.mygov.scot/short-term-let-licences'),
    ('mygov.scot: Types of licence','https://www.mygov.scot/short-term-let-licences/types'),
    ('mygov.scot: Exclusions','https://www.mygov.scot/short-term-let-licences/exclusions'),
    ('mygov.scot: Legal requirements (mandatory conditions)','https://www.mygov.scot/short-term-let-licences/legal-requirements'),
    ('mygov.scot: Apply for a licence','https://www.mygov.scot/short-term-let-licences/apply'),
    ('mygov.scot: Planning permission and control areas','https://www.mygov.scot/short-term-let-licences/planning-permission-control-areas')]
CK=[('Paperwork',['Gas Safety Certificate dated within the last 12 months (if there is gas)','Electrical Installation Condition Report (EICR) for fixed installations','Portable Appliance Testing (PAT) report for appliances guests can use, with tested items labelled','Buildings insurance valid for the length of the licence','Public liability insurance valid for each let','Energy Performance Certificate (EPC) under 10 years old, if letting a whole house or flat (rating goes in every advert)','Floor plan, if your council asks (does not need to be an architect\'s plan)']),
    ('Safety in the property',['Adequate heat and smoke alarms','Carbon monoxide alarms','Fire risk assessment carried out','Fire-fighting equipment, such as a fire blanket, and a fire action plan for guests','Furniture and furnishings meet fire safety rules (keep labels, receipts or photos)','Legionella risk assessed','Repairing standard (including the tolerable standard) met','Private water supply conditions met, if you are not on mains water']),
    ('Displayed for guests',['Certified copy of the licence and its conditions','Fire, gas and electrical safety information','How to contact the emergency services','Copies of the gas safety report, EICR and PAT report','What to do if the carbon monoxide alarm sounds','Instructions for any mobile gas cabinet heaters']),
    ('Application and after',['Check planning: in a control area, letting a whole home that isn\'t your main home very likely needs planning permission','Apply through your council\'s website and pay its fee','Display the public notice at or near the property for 21 days from the date you applied','Once licensed, put the licence number in every advert','Keep guest numbers within the maximum on your licence'])]
FAQ=[('Do I need a short-term let licence in Scotland?','Yes, if you let accommodation to guests on a temporary basis and no exclusion applies. You must have the licence before you take bookings or receive guests. Exclusions include immediate family, tenancies, hotels with hotel planning permission, caravans on licensed holiday sites, aparthotels and bothies.'),
     ('Which type of licence do I need?','There are 4 types. Secondary letting is for a place you do not normally live in, such as a holiday cottage. Home sharing is letting all or part of your home while you live there. Home letting is letting your home while you are away. Home letting and home sharing covers both.'),
     ('How long does a licence last?','A licence usually lasts 3 years.'),
     ('How long does the council take to decide?','Councils must decide within 9 months, unless the sheriff court gives them more time. If they miss the deadline without an extension, they must give you a licence for up to a year while they finish.'),
     ('What happens if I let without a licence?','It is a criminal offence. You can be fined up to £2,500 and banned from applying for a licence for a year.'),
     ('How much does a licence cost?','Each council sets its own fees, based on the property and type of let. Check your council\'s website.'),
     ('Can I let for a short time without a full licence?','Some councils offer temporary licences (up to 6 weeks a year) or temporary exemptions (up to 3 in 12 months, no more than 6 weeks in total). It is up to each council. A provisional licence is available if you are building new accommodation.'),
     ('Can I appeal if I am refused?','Yes, at the sheriff court within 28 days of the decision. You cannot reapply for a year unless your circumstances change materially.')]
cl=''.join(f'<div class="box"><h2>{h}</h2>'+''.join(f'<label class="ck"><input type="checkbox" data-k="{n}-{i}"> {e(x)}</label>' for i,x in enumerate(L))+'</div>' for n,(h,L) in enumerate(CK))
fq=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in FAQ)
ld=_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]}).replace('</','<\\/')
f='scotland-short-term-let-licence-guide.html'
t='How to get a short-term let licence in Scotland: steps and checklist'
dsc='Plain-English steps to get a Scottish short-term let licence, plus a free tick-off checklist of every certificate, safety item and notice you need. Official sources.'
b=f'''{TLDR(['<b>You need the licence first.</b> Every short-term let in Scotland needs a council licence before you take bookings or receive guests, unless an exclusion applies.',
'<b>Letting without one is a criminal offence:</b> a fine of up to £2,500 and a one-year ban from applying.',
'<b>Apply to your council</b> and pay its fee (each council sets its own), then display a public notice at or near the property for 21 days.',
'<b>Councils have up to 9 months to decide.</b> A licence usually lasts 3 years.',
'<b>In a control area</b> (all of Edinburgh, and Badenoch &amp; Strathspey in Highland), a new licence very likely needs planning permission too.',
'<b>Do now:</b> tick off the <a href="#licence-checklist">licence checklist below</a>, and <a href="#get-alerts">get an email</a> if your council\'s fees or rules change.'],sub='From mygov.scot. Not legal advice.')}
<p class="lead">Here are the steps, and a checklist you can tick off as you go (it saves in your browser).</p>
<h2>The steps</h2><ol>
<li><b>Check you need one.</b> Most hosts do. See the exclusions on <a href="https://www.mygov.scot/short-term-let-licences/exclusions" rel="nofollow">mygov.scot</a>.</li>
<li><b>Pick your licence type.</b> Secondary letting, home sharing, home letting, or home letting and home sharing.</li>
<li><b>Check planning.</b> If you are in a control area (all of Edinburgh, and Badenoch &amp; Strathspey in Highland), letting a whole home that isn't your main home very likely needs planning permission. <a href="scotland.html">See Scotland rules</a>.</li>
<li><b>Get your certificates and safety items in place.</b> Use the checklist below.</li>
<li><b>Apply through your council's website</b> and pay its fee. Fees vary by council. Example: <a href="councils/highland.html">Highland fees</a>.</li>
<li><b>Display a public notice</b> at or near the property for 21 days from the date you applied.</li>
<li><b>Wait for a decision.</b> Councils have up to 9 months.</li>
<li><b>Once licensed,</b> put your licence number in every advert and display the required information for guests.</li></ol>
<h2>Licence checklist</h2><p class="small">Ticks are stored only on this device. <button type="button" id="ckp">Print checklist</button> <button type="button" id="ckr">Clear ticks</button></p><p id="ckc" class="small"></p>{cl}
<p class="small">Your council can add its own conditions on top of these. Check its website.</p>
<h2>Common questions</h2>{fq}
{SCOTALERT('scot-licence-guide','We track licence fees, control areas, the visitor levy and licensing rule changes for Scottish councils against official sources, and email you when one changes, so you hear about it before your application or renewal.')}
<p>Related: <a href="scotland-business-rates-checker.html">Business rates or council tax checker</a> · <a href="uk-visitor-levy-map.html">UK visitor levy map</a> · <a href="councils.html">Council pages</a></p>
<p>Fire safety in detail: <a href="short-term-let-fire-safety-scotland.html">alarms, doors, the fire risk assessment and a checklist</a>.</p>
<h2>Official sources</h2><ul>{"".join(f'<li><a href="{u}" rel="nofollow">{e(n)}</a></li>' for n,u in GS)}</ul>
<p class="small"><b>Not legal advice.</b> Summarised from mygov.scot, checked {C}.</p>
<script>(function(){{var K='stl-scot-ck',s={{}};try{{s=JSON.parse(localStorage.getItem(K))||{{}}}}catch(x){{}}
var b=document.querySelectorAll('.ck input'),c=document.getElementById('ckc');function n(){{var d=0;b.forEach(function(i){{if(i.checked)d++}});c.textContent=d+' of '+b.length+' done';}}
b.forEach(function(i){{i.checked=!!s[i.dataset.k];i.addEventListener('change',function(){{s[i.dataset.k]=i.checked;try{{localStorage.setItem(K,JSON.stringify(s))}}catch(x){{}}n();}})}});
document.getElementById('ckp').onclick=function(){{window.print()}};document.getElementById('ckr').onclick=function(){{s={{}};b.forEach(function(i){{i.checked=false}});try{{localStorage.removeItem(K)}}catch(x){{}}n();}};n();}})();</script>'''
page(f,t,b,desc=dsc,full_title=t+' | UK Short-Let Rules Tracker',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{ld}</script>')
