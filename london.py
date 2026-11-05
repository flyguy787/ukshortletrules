# ---- London 90-night counter ----
LS=[('Deregulation Act 2015, s.44 (inserts s.25A and s.25B into the Greater London Council (General Powers) Act 1973)','https://www.legislation.gov.uk/ukpga/2015/20/section/44'),
    ('Airbnb: responsible hosting in the UK (London 90-night rule)','https://www.airbnb.co.uk/help/article/1379'),
    ('Airbnb: London 90-night limit explained','https://www.airbnb.co.uk/help/article/1340'),
    ('Airbnb: night limits FAQ (how nights are counted)','https://www.airbnb.co.uk/help/article/1628')]
LFAQ=[('What is the London 90-night rule?','In Greater London, using a home as temporary sleeping accommodation is normally a material change of use that needs planning permission. Since 26 May 2015 there is an exception: no planning permission is needed if the total nights of that use in a calendar year do not exceed 90, and the person providing the accommodation is liable for council tax on the property.'),
      ('Does the 90-night limit reset each year?','Yes. The law counts nights in the same calendar year, so the count runs from 1 January to 31 December.'),
      ('Do nights on different platforms count together?','Yes. The law counts every night the premises are used as temporary sleeping accommodation in the calendar year, whoever provided it, so nights booked through Airbnb, Booking.com, Vrbo or directly all add up. Platform counters only see their own bookings.'),
      ('Does it apply if I let a room in my home?','Airbnb applies its automatic 90-night cap to entire-home listings in Greater London. If you are only letting part of your home while you live there, check with your borough planning team.'),
      ('Do long stays count towards the 90 nights?','Airbnb says reservations of 90 days or more are not short-term stays under the 2015 Deregulation Act and do not count towards its London limit.'),
      ('What if I want to let for more than 90 nights?','You would need planning permission from your borough. Airbnb lets hosts with permission claim an exemption in the listing\'s Regulations tab, which removes its automatic cap.'),
      ('Can a borough switch the 90-night exception off?','Yes. A borough (with the Secretary of State\'s consent) or the Secretary of State can direct that the exception does not apply to particular premises or areas, if needed to protect local amenity.')]
fq=''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q,a in LFAQ)
ld=_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in LFAQ]}).replace('</','<\\/')
# (3 Nov 2026) While #ln-alert shows, the static mid-page #london-alert box is hidden too (one London signup at a time).
# In-context alert signup under the 90-night result (data-cta london90-result), like renewal-result/occupancy-result (2 Nov 2026).
# Shown once at least one booking has nights in the chosen year; always pre-set to council:greater-london-all-boroughs (the London area the
# page's own picker and the buyer checker use). Reason restates facts already sourced on this page: the 90-night limit and planning permission
# above it (Deregulation Act 2015 s44), a borough/Secretary of State can switch the exception off, and the England register GOV.UK expects in March 2027.
LNALERT='<div class="alertbox" id="ln-alert" hidden><h2>Get an email when the 90-night rule or other London short-let rules change</h2><p id="ln-why">We track these rules against official sources and email you when one of them changes.</p><p class="small">Plus one short weekly UK "what changed" email. Free. Unsubscribe any time.</p>'+FORMX.replace('<form class="signup"','<form class="signup" id="ln-form" data-cta="london90-result" data-area="council:greater-london-all-boroughs" data-area-name="Greater London (all boroughs)"',1).replace('>Subscribe<','>Get free alerts<')+'</div>'
LNJS='''<script>(function(){var SEEN={},RK='',W={over:'Above 90 nights in a calendar year you need planning permission from your borough (Deregulation Act 2015, s44). We watch the 90-night rule, and the England-wide changes that also apply in London such as the national short-term let register GOV.UK expects to begin in March 2027, against official sources, and email you when something changes.',
under:'The 90-night limit is set in law (Deregulation Act 2015, s44), and a borough or the Secretary of State can switch the exception off for specific properties or areas. We watch it, and the England-wide changes that also apply in London such as the national short-term let register GOV.UK expects to begin in March 2027, against official sources, and email you when something changes.'};
function band(u){return u<1?'0':u<=30?'1-30':u<=60?'31-60':u<=80?'61-80':u<=90?'81-90':'91+'}
function sw(){var A=document.getElementById('ln-alert'),L=document.getElementById('london-alert'),S=document.querySelector('section.alertcta');if(L)L.hidden=!A.hidden;if(S)S.hidden=!A.hidden;else if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',sw)}
window.lnA=function(u,rows,y){var A=document.getElementById('ln-alert'),F=document.getElementById('ln-form');if(!A||!F)return;
if(!rows){if(!A.hidden){A.hidden=true;sw()}RK='';return}
var ov=u>90,b=band(u),rk=y+'|'+b;if(rk!==RK){var M=F.querySelector('.msg');if(M)M.textContent=''}RK=rk;
document.getElementById('ln-why').textContent=W[ov?'over':'under'];A.hidden=false;sw();
var k=b+'|'+(ov?'yes':'no');if(!SEEN[k]){SEEN[k]=1;try{gtag('event','london90_check',{nights_band:b,over_limit:ov?'yes':'no'})}catch(x){}}};})();</script>'''
f='london-90-night-counter.html'
t='London 90-night rule counter for short-term lets'
dsc='Free London 90-night counter: add your bookings from every platform and see how many short-let nights you have left this calendar year without planning permission. Official sources.'
b=f'''<p class="lead">In Greater London you can let a whole home short-term for up to <b>90 nights per calendar year</b> without planning permission. Add your bookings from every platform below to see how many nights you have left. Your bookings stay on this device only.</p>
<div class="box"><p><label><b>Calendar year</b> <input type="number" id="ly" min="2015" max="2100" inputmode="numeric" style="width:6em"></label></p>
<p><label>Check-in <input type="date" id="lin"></label> <label>Check-out <input type="date" id="lout"></label> <label>Platform <input type="text" id="lp" placeholder="e.g. Airbnb" style="width:9em"></label> <button type="button" id="ladd">Add booking</button></p>
<p id="lerr" class="small" aria-live="polite"></p>
<div class="tw"><table id="lt"><tr><th>Check-in</th><th>Check-out</th><th>Platform</th><th>Nights in year</th><th></th></tr></table></div>
<div id="lres" aria-live="polite"></div>{LNALERT}
<p class="small"><button type="button" id="lclr">Clear all bookings</button> <button type="button" onclick="window.print()">Print</button></p></div>
<h2>How the counter works</h2><ul>
<li>It counts the nights of each stay that fall in the year you choose. A stay over New Year is split across the two years.</li>
<li>Stays of <b>90 nights or more</b> are shown but not counted, in line with how Airbnb applies the rule. Check with your borough if you rely on this.</li>
<li>Add bookings from <b>every</b> platform and direct bookings. The law counts all nights at the property, so Airbnb's own counter can show fewer nights than you have really used.</li></ul>
<h2>The rule in brief</h2><ul>
<li>Applies to residential premises in <b>Greater London</b> (all 32 boroughs and the City of London). In force since 26 May 2015.</li>
<li>Two conditions: no more than <b>90 nights in the calendar year</b> in total, and the person providing the accommodation is <b>liable for council tax</b> on the property for each night.</li>
<li>A borough or the Secretary of State can switch the exception off for specific properties or areas.</li>
<li>Above 90 nights you need <b>planning permission</b> from your borough. Airbnb blocks further short-term bookings on entire-home listings once 90 nights are booked, unless you claim an exemption.</li>
<li>England has no short-let licence or registration scheme in force. <a href="england.html">See England rules</a>.</li>
<li>Buying a London property to let? Check the 90-night limit, lease, lender consent and insurance first with our <a href="buyer-due-diligence-checker?council=greater-london-all-boroughs">buyer due-diligence checker for Greater London</a>.</li></ul>
{TOPICALERT('london-alert','london-90-night','Get an email when short-let rules change in London',
 'The 90-night rule is set in law (<a href="https://www.legislation.gov.uk/ukpga/2015/20/section/44" rel="nofollow">Deregulation Act 2015, s44</a>). We watch it, and the England-wide changes that also apply in London, against official sources, and email you when something changes.',
 "Next dates for London hosts we're watching",_rowdates(lambda r:r[2] in ('All of England','England, Wales and Northern Ireland')),
 [('council:greater-london-all-boroughs','Greater London (all boroughs)',True),('nation:england','England',False)],'Your area',
 'Keep Greater London for London alerts, or pick All of England.',
 'We have no upcoming London dates logged right now. If the government or a borough announces a change, we\'ll email you.')}
<h2>Common questions</h2>{fq}
<p>Related: <a href="councils/greater-london-all-boroughs.html">Greater London council page</a> · <a href="london-second-homes-council-tax-premium.html">London second homes premium by borough</a> · <a href="uk-visitor-levy-map.html">UK visitor levy map</a> · <a href="changes.html">Changes log</a> · <a href="buyer-due-diligence-checker?council=greater-london-all-boroughs">Buying a holiday let? Due-diligence checker</a></p>
<h2>Official sources</h2><ul>{"".join(f'<li><a href="{u}" rel="nofollow">{e(n)}</a></li>' for n,u in LS)}</ul>
<p class="small"><b>Not legal or planning advice.</b> Checked {C}. Your borough planning team has the final say.</p>
{LNJS}<script>
function lnNights(i,o,y){{var a=new Date(i+'T00:00:00Z'),b=new Date(o+'T00:00:00Z');if(isNaN(a)||isNaN(b)||b<=a)return null;var D=864e5,tot=Math.round((b-a)/D),s=Math.max(a,Date.UTC(y,0,1)),en=Math.min(b,Date.UTC(y+1,0,1));return {{total:tot,inYear:Math.max(0,Math.round((en-s)/D))}};}}
(function(){{var K='stl-ldn-90',L=[];try{{L=JSON.parse(localStorage.getItem(K))||[]}}catch(x){{}}
var Y=document.getElementById('ly'),T=document.getElementById('lt'),R=document.getElementById('lres'),E=document.getElementById('lerr');Y.value=new Date().getFullYear();
function sv(){{try{{localStorage.setItem(K,JSON.stringify(L))}}catch(x){{}}}}
function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function draw(){{var y=parseInt(Y.value,10),u=0,nr=0;while(T.rows.length>1)T.deleteRow(1);
L.slice().sort(function(p,q){{return p.i<q.i?-1:1}}).forEach(function(k){{var n=lnNights(k.i,k.o,y);if(!n||n.inYear==0)return;nr++;var long=n.total>=90;if(!long)u+=n.inYear;
var r=T.insertRow();r.innerHTML='<td>'+esc(k.i)+'</td><td>'+esc(k.o)+'</td><td>'+esc(k.p||'')+'</td><td>'+(long?n.inYear+' <span class="tag">90+ night stay, not counted</span>':n.inYear)+'</td><td><button type="button">Remove</button></td>';
r.querySelector('button').onclick=function(){{L.splice(L.indexOf(k),1);sv();draw();}};}});
var left=90-u,c=u>90?'warn':'';R.innerHTML='<h2>'+u+' of 90 nights used in '+y+'</h2><p>'+(u>90?'<span class="tag warn">Over the limit</span> You are '+(u-90)+' nights over. Above 90 nights you need planning permission from your borough.':left<=10?'<span class="tag warn">Nearly there</span> '+left+' nights left this calendar year.':left+' nights left this calendar year.')+'</p>';if(window.lnA)lnA(u,nr,y);}}
document.getElementById('ladd').onclick=function(){{var i=document.getElementById('lin').value,o=document.getElementById('lout').value,p=document.getElementById('lp').value.slice(0,40);
if(!lnNights(i,o,2000)){{E.textContent='Pick a check-in date and a later check-out date.';return;}}E.textContent='';L.push({{i:i,o:o,p:p}});sv();draw();}};
document.getElementById('lclr').onclick=function(){{if(confirm('Remove all bookings from this device?')){{L=[];sv();draw();}}}};Y.oninput=draw;draw();}})();</script>'''
page(f,t,b,desc=dsc,full_title='London 90-night rule counter (free) | UK Short-Let Rules Tracker',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{ld}</script>')
