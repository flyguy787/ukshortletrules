# Visitor levy calculator + embeddable widget. Rules only from official sources (checked 23 Oct 2026).
import json as _j
LV=[
 dict(id='edinburgh',name='City of Edinburgh',kind='pct',rate=5,start='2026-07-24',cut='2025-10-01',cutpaid=True,cap=5,capkind='charge',
  rule='5% of the accommodation-only cost (net of VAT), first 5 consecutive nights only. Stays from 24 Jul 2026. Bookings paid for (in part or full) before 1 Oct 2025 are exempt. Stays that began before 24 Jul 2026 are not liable.',
  src=['https://www.edinburgh.gov.uk/visitorlevyinformation','https://www.visitscotland.org/tourism-events-industry/visitor-levy']),
 dict(id='glasgow',name='Glasgow City',kind='pct',rate=5,start='2027-01-25',cut='2026-04-01',cutpaid=False,cap=0,
  rule='5% of the accommodation-only cost (net of VAT), whole stay. Stays from 25 Jan 2027. Bookings made on or after 1 Apr 2026 are liable.',
  src=['https://www.glasgow.gov.uk/article/14800/Accommodation-providers','https://www.visitscotland.org/tourism-events-industry/visitor-levy']),
 dict(id='aberdeen',name='Aberdeen City',kind='pct',rate=7,start='2027-04-01',cut='2026-10-01',cutpaid=True,cap=0,
  rule='7% of the accommodation cost, whole stay. Stays from 1 Apr 2027. Exempt only if the booking was made and a payment (any amount, including a deposit) was received before 1 Oct 2026.',
  src=['https://www.aberdeencity.gov.uk/Council-Services/business-and-investment/introducing-the-aberdeen-visitor-levy/information-for-businesses','https://www.visitscotland.org/tourism-events-industry/visitor-levy']),
 dict(id='stirling',name='Stirling',kind='pct',rate=3,start='2027-06-14',cut='2027-01-01',cutpaid=True,cap=7,capkind='refund',
  rule='3% of the accommodation-only cost (net of VAT). Stays from 14 Jun 2027, bookings made on or after 1 Jan 2027. Charged on every night, but the guest can claim a refund for nights beyond 7 in one booking. Stirling council-tax-registered residents who booked and paid themselves can claim a refund.',
  src=['https://www.stirling.gov.uk/about-the-council/stirling-visitor-levy-scheme/details-about-stirlings-visitor-levy-scheme/','https://www.stirling.gov.uk/about-the-council/stirling-visitor-levy-scheme/information-on-exemptions/']),
 dict(id='west-dunbartonshire',name='West Dunbartonshire',kind='pct',rate=5,start='2027-07-01',cut='2026-10-01',cutpaid=True,cap=0,
  rule='5% of the accommodation cost before VAT, whole stay. Stays from 1 Jul 2027. Stays booked and paid for (in part or full) before 1 Oct 2026 are not liable.',
  src=['https://www.west-dunbarton.gov.uk/business/visitor-levy','https://www.visitscotland.org/tourism-events-industry/visitor-levy']),
 dict(id='cardiff',name='Cardiff',kind='pp',rate=1.30,low=0.75,start='2027-04-01',cut='2026-09-28',cutpaid=False,cap=0,
  rule='£1.30 per person per night (all ages, including babies) for self-catering, holiday lets, B&Bs and hotels; 75p per adult per night in tent pitches or shared hostel rooms (under-18s free there). Stays from 1 Apr 2027; bookings made from 28 Sep 2026 are liable. One booking of 32 nights or more pays no levy.',
  src=['https://www.gov.wales/visitor-levy-accommodation-providers-steps/how-much','https://www.gov.wales/visitor-levy-accommodation-providers-steps/before-levy-starts','https://www.gov.wales/check-if-local-council-charges-visitor-levy-wales']),
]
LVJ=_j.dumps(LV)
LVF='''<form class="lvf" id="lvf" onsubmit="return false"><div class="ckw">
<label for="lc">Council</label><select id="lc">%s</select>
<label for="lb">Booking date (when the guest booked)</label><input type="date" id="lb" required>
<div id="lpw"><label><input type="checkbox" id="lp"> A payment (deposit or more) was made before <span id="lcd"></span></label></div>
<label for="li">Check-in</label><input type="date" id="li" required>
<label for="lo">Check-out</label><input type="date" id="lo" required>
<div id="lpw2"><label for="lpr">Nightly price, accommodation only, excluding VAT (£)</label><input type="number" id="lpr" min="0" step="0.01" inputmode="decimal"></div>
<div id="lgw" hidden><label for="lt">Accommodation type</label><select id="lt"><option value="hi">Holiday let, self-catering, B&amp;B, hotel or other</option><option value="lo">Tent pitch or shared hostel/dorm room</option></select>
<label for="la">Adults (18+)</label><input type="number" id="la" min="0" value="2" inputmode="numeric">
<label for="lk">Children (under 18, including babies)</label><input type="number" id="lk" min="0" value="0" inputmode="numeric"></div>
<button type="button" id="lgo">Work out the levy</button></div></form>
<div id="lr" aria-live="polite" hidden><h2 id="lrh"></h2><p id="lrt"></p><h3>Guest message (copy and paste)</h3><textarea id="lmsg" rows="3" style="width:100%%" aria-label="Guest message"></textarea><p><button type="button" id="lcp">Copy message</button> <span id="lcm" class="small"></span></p><p class="small" id="lsrc"></p><p class="small"><b>Estimate, not tax advice.</b> Based on the council's published scheme; the accommodation provider is responsible for the correct amount. Check the official source.</p></div>'''%''.join(f'<option value="{x["id"]}">{x["name"]}</option>' for x in LV)
LVJS='''<script>(function(){var L=__L__,$=function(i){return document.getElementById(i)};
function cur(){var v=$('lc').value;for(var i=0;i<L.length;i++)if(L[i].id==v)return L[i]}
function fd(s){var d=new Date(s+'T00:00:00Z');return d.toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric',timeZone:'UTC'})}
function sync(){var c=cur();$('lpw').hidden=!c.cutpaid;$('lcd').textContent=fd(c.cut);$('lgw').hidden=c.kind!='pp';$('lpw2').hidden=c.kind=='pp'}
$('lc').addEventListener('change',sync);sync();
function src(c){return 'Sources: '+c.src.map(function(u){return '<a href="'+u+'" target="_blank" rel="noopener nofollow">'+u.replace(/^https:\\/\\/(www\\.)?/,'').split('/')[0]+'</a>'}).join(', ')}
$('lgo').addEventListener('click',function(){var c=cur(),b=$('lb').value,ci=$('li').value,co=$('lo').value,r=$('lr');
 if(!b||!ci||!co){alert('Please enter the booking date, check-in and check-out.');return}
 var n=Math.round((Date.parse(co)-Date.parse(ci))/864e5);if(n<1){alert('Check-out must be after check-in.');return}
 var day=864e5,s=Date.parse(c.start),liable=0,i,why='',amt=0,refund=0,first=Date.parse(ci);
 for(i=0;i<n;i++)if(first+i*day>=s)liable++;
 if(c.id=='edinburgh'&&first<s){liable=0;why='The stay starts before 24 Jul 2026, so the council says it is not liable.'}
 else if(liable==0)why='The whole stay is before the levy starts on '+fd(c.start)+'.';
 else if(b<c.cut&&(!c.cutpaid||$('lp').checked))why='Booked before '+fd(c.cut)+(c.cutpaid?' with a payment made before then':'')+', so the advance-booking rule exempts this stay.';
 else if(c.id=='cardiff'&&n>=32)why='One booking of 32 nights or more pays no Welsh visitor levy.';
 var msg;
 if(why){$('lrh').textContent='No levy due';$('lrt').textContent=why;msg='Good news: your stay is not subject to the '+c.name+' visitor levy.'}
 else{var note='';
  if(c.kind=='pct'){var p=parseFloat($('lpr').value);if(!(p>=0)){alert('Please enter the nightly price.');return}
   var nn=liable;if(c.cap&&c.capkind=='charge'&&nn>c.cap){nn=c.cap;note=' Only the first '+c.cap+' nights are charged.'}
   amt=p*nn*c.rate/100;if(c.cap&&c.capkind=='refund'&&liable>c.cap){refund=p*(liable-c.cap)*c.rate/100;note=' The guest can claim back £'+refund.toFixed(2)+' for nights beyond '+c.cap+'.'}
   if(liable<n)note+=' '+(n-liable)+' night(s) fall before the start date and are not counted (check with the council how stays spanning the start date are treated).';
   $('lrt').textContent=c.rate+'% of £'+(p*nn).toFixed(2)+' ('+nn+' night'+(nn>1?'s':'')+' × £'+p.toFixed(2)+').'+note;
   msg='Your stay includes the '+c.name+' visitor levy of £'+amt.toFixed(2)+' ('+c.rate+'% of the accommodation cost'+(c.capkind=='charge'&&c.cap?', first '+c.cap+' nights':'')+'), which we collect and pay to the council.'+(refund?' You can claim a refund of £'+refund.toFixed(2)+' for nights beyond '+c.cap+' from Stirling Council.':'')}
  else{var a=parseInt($('la').value||0),k=parseInt($('lk').value||0),lo=$('lt').value=='lo',ppl=lo?a:a+k,rt=lo?c.low:c.rate;amt=ppl*liable*rt;
   $('lrt').textContent='£'+rt.toFixed(2)+' × '+ppl+' '+(lo?'adult':'guest')+(ppl==1?'':'s')+' × '+liable+' night'+(liable>1?'s':'')+'.'+(lo&&k?' Under-18s are not charged in tent pitches or shared hostel rooms.':'')+(liable<n?' '+(n-liable)+' night(s) before 1 Apr 2027 not counted.':'');
   msg='Your stay includes the Welsh visitor levy for Cardiff of £'+amt.toFixed(2)+' (£'+rt.toFixed(2)+' per person per night), which we pay to the Welsh Revenue Authority.'}
  $('lrh').textContent='Levy due: £'+amt.toFixed(2)}
 $('lmsg').value=msg;$('lsrc').innerHTML=src(c)+'. Rule: '+c.rule.replace(/</g,'&lt;');r.hidden=false;$('lrh').focus&&r.scrollIntoView({block:'nearest'})});
$('lcp').addEventListener('click',function(){var t=$('lmsg');t.select();(navigator.clipboard?navigator.clipboard.writeText(t.value):Promise.reject()).then(function(){$('lcm').textContent='Copied.'},function(){document.execCommand('copy');$('lcm').textContent='Copied.'})});
})();</script>'''.replace('__L__',LVJ)
rows=''.join(f'<tr><td>{x["name"]}</td><td>{e(x["rule"])}</td><td>{" ".join(f"<a href=\"{u}\" rel=\"nofollow\">source</a>" for u in x["src"])}</td></tr>' for x in LV)
LVSNIP=f'<iframe src="{SITE}levy-calculator-widget.html" title="UK visitor levy calculator" width="100%" height="760" style="border:1px solid #ccd;border-radius:8px;max-width:640px" loading="lazy"></iframe>\n<p style="font-size:13px">Levy calculator by <a href="{SITE}">UK Short-Let Rules</a></p>'
page('levy-calculator.html','Visitor levy calculator for short-let hosts',f'''<p class="lead">Work out the visitor levy on a booking in Edinburgh, Glasgow, Aberdeen, Stirling, West Dunbartonshire or Cardiff, check whether the advance-booking rules exempt it, and copy a ready-made line for your guest. Rules from each council's published scheme, checked {C}.</p>
<div class="card">{LVF}</div>
<h2>Rules used</h2><div class="tw"><table><tr><th>Council</th><th>Rule</th><th>Official source</th></tr>{rows}</table></div>
<p class="small">Percentage levies apply to the accommodation-only part of the price, net of VAT: leave out optional extras like meals, parking or paid laundry. Exempt guests (for example some disability benefit recipients in Scotland) usually pay and then claim a refund from the council. Highland, Dundee and others are still consulting, so they are not in the calculator: see the <a href="uk-visitor-levy-map.html">levy map</a>. Manchester and Liverpool accommodation BID charges are not statutory levies and are not included.</p>
{LEVYALERT('levy-calculator','levy-alert')}
<h2>Embed this calculator</h2><p>Free for agents, hosts and bloggers. No tracking, no cookies.</p><textarea readonly rows="4" style="width:100%" aria-label="Embed code">{e(LVSNIP)}</textarea>
{LVJS}''',desc='Free visitor levy calculator for Edinburgh, Glasgow, Aberdeen, Stirling, West Dunbartonshire and Cardiff: levy due, advance-booking exemptions, a guest message and official sources.',full_title='Visitor levy calculator: Edinburgh, Glasgow, Cardiff and more | UK Short-Let Rules')
open('levy-calculator-widget.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Visitor levy calculator | UK Short-Let Rules</title><meta name="robots" content="noindex"><link rel="canonical" href="{SITE}levy-calculator.html"><style>body{{margin:0;padding:.8rem;font:15px/1.5 system-ui,sans-serif;color:#1d2433;background:#fff}}h1{{font-size:1.1rem;margin:0 0 .5rem;color:#123c5a}}h2{{font-size:1.05rem;margin:.8rem 0 .3rem}}h3{{font-size:.95rem}}a{{color:#155a8a}}:focus-visible{{outline:3px solid #f2a541;outline-offset:2px}}.small{{font-size:.8rem;color:#556}}.ckw label{{display:block;font-weight:600;margin-top:.5rem}}.ckw input,.ckw select{{font:inherit;padding:.35rem;max-width:100%}}button{{font:inherit;background:#f2a541;color:#1b2533;border:0;border-radius:8px;padding:.5rem .9rem;margin-top:.7rem;cursor:pointer}}footer{{margin-top:.8rem;font-size:.8rem;color:#556}}</style></head><body><main><h1>Visitor levy calculator</h1>{LVF}{LVJS}</main><footer>Free calculator by <a href="{SITE}levy-calculator.html" target="_blank" rel="noopener">UK Short-Let Rules</a>. Rules last checked {C}.</footer></body></html>''')
