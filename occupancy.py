# Occupancy threshold tracker (business rates tests). Sources checked 23 Oct 2026.
OC=dict(
 wales=dict(name='Wales',let=182,av=252,period='any 12-month period (the one you use for your claim)',
  allow=['Stays of 28 nights or less count. Nights in stays over 28 nights do not count towards the 182 let nights, but can count towards the 252 available nights if the property could have been booked for 28 nights or less.',
   'Averaging: if you own several self-catering lets in the same location or very near each other, you can average nights let across them.',
   'From 1 Apr 2026 you can use the average nights let over the previous 24 or 36 months (at least 182 a year on average).',
   'From 1 Apr 2026 up to 14 nights a year donated to a registered charity can count.',
   'Not counted: nights closed for repair or refurbishment, site closures, your own use or discounted lets to friends and family, and future bookings that have not happened yet.'],
  miss='The property may be moved from business rates to council tax, where Welsh councils can charge a second homes premium.',
  src=['https://www.gov.uk/guidance/apply-for-business-rates-for-a-self-catering-property-in-wales']),
 england=dict(name='England',let=70,av=140,period='a 12-month period (the one you use for your claim)',
  allow=['Nights in stays over 28 nights do not count towards the 70 let nights, but can count towards the 140 available nights if the property could have been booked for 28 nights or less.',
   'From 24 Jul 2026, 5 or more self-catering lets that are part of the same property qualify if none is a main residence and you intend to make each available for 140 days in the next 12 months; the 140/70 history test does not apply to them.',
   'A holiday let sharing land with a different business run by the same owner can qualify on intention alone (140 days in the next 12 months).',
   'Not counted: nights closed for repair or refurbishment, site closures, your own use or discounted lets to friends and family, and future bookings that have not happened yet.'],
  miss='The property is valued for council tax instead of business rates. Many councils charge a second homes premium (up to 100%) on furnished homes nobody lives in.',
  src=['https://www.gov.uk/guidance/apply-for-business-rates-for-a-self-catering-property-in-england']),
 scotland=dict(name='Scotland',let=70,av=140,period='the financial year (1 April to 31 March)',
  allow=['The property must not be anyone\'s only or main residence and must be let commercially, with a view to profit, for short periods.',
   'Lets to family and friends that are not commercial do not count towards the 70 nights.',
   'Bookings over 28 nights need an explanation in your evidence to the Assessor.',
   'Evidence for each financial year must reach the Assessor before 27 May the following year (or within 56 days of an Assessor request, if later).'],
  miss='No evidence, late evidence or evidence that falls short means the property goes on the council tax list for that year, where councils can charge a second homes premium.',
  src=['https://www.mygov.scot/non-domestic-rates-guidance/short-term-lets','https://www.legislation.gov.uk/ssi/2026/72/made','https://www.saa.gov.uk/non-domestic-valuation/self-catering/']),
)
import json as _j
_opts=''.join(f'<option value="{k}">{v["name"]} ({v["av"]} available / {v["let"]} let)</option>' for k,v in OC.items())
OCJS='''<script>(function(){var O=__O__,$=function(i){return document.getElementById(i)};
function fd(d){return d.toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'})}
function sync(){var o=O[$('on').value];$('ope').textContent='Counting period: '+o.period+'.';if($('on').value=='scotland'&&!$('oe').value){var t=new Date(),y=t.getMonth()>2?t.getFullYear()+1:t.getFullYear();$('oe').value=y+'-03-31'}}
$('on').addEventListener('change',sync);sync();
$('ogo').addEventListener('click',function(){var o=O[$('on').value],l=parseInt($('ol').value||0),a=parseInt($('oa').value||0),e=$('oe').value;
 if(!e){alert('Please enter the end date of your 12-month period.');return}
 var end=new Date(e+'T23:59:59'),now=new Date(),left=Math.max(0,Math.ceil((end-now)/864e5)),nl=Math.max(0,o.let-l),na=Math.max(0,o.av-a);
 var h,ok=nl==0&&na==0;
 if(ok)h='You have reached both thresholds ('+o.av+' available, '+o.let+' let).';
 else h='You need '+(nl?nl+' more let night'+(nl>1?'s':''):'no more let nights')+(na?' and '+na+' more available night'+(na>1?'s':''):'')+' by '+fd(end)+'.';
 var warn=(!ok&&(nl>left||na>left))?' There are only '+left+' nights left in the period, so the shortfall cannot be made up from new nights alone.':(!ok?' '+left+' nights left in the period.':'');
 $('orh').textContent=h;$('orw').textContent=warn;
 $('oal').innerHTML=o.allow.map(function(x){return '<li>'+x+'</li>'}).join('');$('omiss').textContent=o.miss;
 $('osrc').innerHTML='Sources: '+o.src.map(function(u){return '<a href="'+u+'" rel="nofollow">'+u.replace('https://','').split('/')[0]+'</a>'}).join(', ');
 var body='Holiday let business rates check ('+o.name+')\\n\\nThreshold: '+o.av+' nights available and '+o.let+' nights let in '+o.period+'.\\nSo far: '+a+' available, '+l+' let.\\nPeriod ends: '+fd(end)+'.\\nResult: '+h+warn+'\\nIf missed: '+o.miss+'\\n\\nSource: '+o.src[0]+'\\nWorked out with the free tracker at https://ukshortletrules.co.uk/occupancy-threshold-tracker (general information, not tax advice).';
 $('omail').href='mailto:?subject='+encodeURIComponent('Holiday let business rates threshold: '+o.name)+'&body='+encodeURIComponent(body);
 $('or').hidden=false});
})();</script>'''.replace('__O__',_j.dumps(OC))
_tab=''.join(f'<tr><td>{v["name"]}</td><td>{v["av"]} nights</td><td>{v["let"]} nights</td><td>{v["period"]}</td><td>{" ".join(f"<a href=\"{u}\" rel=\"nofollow\">source</a>" for u in v["src"])}</td></tr>' for v in OC.values())
page('occupancy-threshold-tracker.html','Holiday let occupancy threshold tracker',f'''<p class="lead">Are you on track for business rates? Enter your nights so far and the end of your 12-month period to see how many more let nights you need, the allowances that apply and what happens if you miss. Rules from GOV.UK, mygov.scot and the Scottish Assessors, checked {C}.</p>
<div class="card"><form class="lvf" onsubmit="return false">
<label for="on">Where is the property?</label><select id="on">{_opts}</select><p class="small" id="ope"></p>
<label for="ol">Nights let so far (stays of 28 nights or less)</label><input type="number" id="ol" min="0" max="366" inputmode="numeric" value="0">
<label for="oa">Nights available to let so far</label><input type="number" id="oa" min="0" max="366" inputmode="numeric" value="0">
<label for="oe">End date of the 12-month period</label><input type="date" id="oe">
<button type="button" id="ogo">Check my nights</button></form>
<div id="or" hidden aria-live="polite"><h2 id="orh"></h2><p id="orw"></p><h3>Allowances and what counts</h3><ul id="oal"></ul><h3>If you miss the threshold</h3><p id="omiss"></p><p><a class="btn" id="omail" href="#">Send to my accountant</a> <span class="small">Opens your email app with a summary. Nothing is sent by this site.</span></p><p class="small" id="osrc"></p><p class="small"><b>Estimate, not tax advice.</b> The valuation office or Assessor decides. Keep booking records as evidence.</p></div></div>
<h2>Thresholds</h2><div class="tw"><table><tr><th>Nation</th><th>Available</th><th>Let</th><th>Period</th><th>Official source</th></tr>{_tab}</table></div>
<p>Northern Ireland uses a different system: see the <a href="northern-ireland.html">Northern Ireland page</a>. For Scotland, try the <a href="scotland-business-rates-checker.html">Scotland business rates checker</a>.</p>{OCJS}''',desc='Free tracker for the holiday let business rates tests: Wales 252/182 nights, England and Scotland 140/70. See how many more let nights you need, allowances, and email a summary to your accountant.',full_title='Holiday let occupancy threshold tracker (182/252 and 140/70 nights) | UK Short-Let Rules')
