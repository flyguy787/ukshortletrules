# ---- Guide: Making Tax Digital for Income Tax for holiday-let / short-let hosts ----
# Facts checked 7 Nov 2026 against GOV.UK. Anything else marked UNVERIFIED.
import json as _j
MTD_FIND='https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax'
MTD_QI='https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax'
MTD_Q='https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates'
MTD_SIGN='https://www.gov.uk/guidance/sign-up-for-making-tax-digital-for-income-tax'
MTD_EX='https://www.gov.uk/guidance/find-out-if-you-can-get-an-exemption-from-making-tax-digital-for-income-tax'
_CHECKED='7 Nov 2026'
f='making-tax-digital-holiday-lets.html'
t='Making Tax Digital for holiday lets'
dsc='Making Tax Digital for Income Tax for UK holiday-let hosts: £50k/£30k/£20k thresholds, free qualifying-income checker, quarterly update dates and what to do now. HMRC sources.'
# FAQ (visible + FAQPage JSON-LD)
MQ=[('Do holiday lets count for Making Tax Digital for Income Tax?','Yes. Holiday-let income is property income. The furnished holiday lettings (FHL) tax regime ended from April 2025, so holiday-let income is treated like other property income and counts towards your qualifying income for Making Tax Digital.'),
 ('What is qualifying income?','Your total gross income from self-employment and from property, before expenses (turnover). It is not your profit. Joint property income counts only as your share. PAYE employment, dividends (including from your own company), pensions, REIT/PAIF income and partnership profit share as an individual partner do not count.'),
 ('When do I have to start Making Tax Digital?','If your qualifying income was over £50,000 in 2024 to 2025, you should have started from 6 April 2026 (you can still sign up). Over £30,000 in 2025 to 2026 means from 6 April 2027. Over £20,000 in 2026 to 2027 means from 6 April 2028. Partnerships have a later timeline that HMRC has not set yet.'),
 ('What are the quarterly update deadlines?','For the standard tax-year periods: 6 April to 5 July due by 7 August; 6 April to 5 October due by 7 November; 6 April to 5 January due by 7 February; 6 April to 5 April due by 7 May the next year. Calendar accounting periods (1 April to 31 March) use the same four deadlines. Quarterly updates are summaries of digital records sent by software, not a full tax return.'),
 ('Are there penalties for late quarterly updates?','For the 2026 to 2027 tax year there are no penalty points for late quarterly updates, but you still need to send the updates before your software tax return. Late Self Assessment return penalties still apply. After 2026 to 2027, a late quarterly update can give a penalty point; four points lead to a £200 penalty.'),
 ('Do I still need a Self Assessment return?','Yes. You still need to submit a Self Assessment tax return for the tax year before you start Making Tax Digital. To sign up you must be registered for Self Assessment and have submitted a tax return in the last 2 years.'),
 ('What if I am digitally excluded or think I am exempt?','Some people are exempt, for example if they are digitally excluded. Exempt people still report income and gains on a Self Assessment tax return. Check HMRC\'s exemption guidance on GOV.UK and apply before you need to start if you think an exemption applies.'),
 ('Is this tax advice?','No. This page is general information from HMRC and GOV.UK guidance, checked on 7 November 2026. Use HMRC\'s official check tool and speak to an accountant or HMRC about your own figures before acting.')]
_mld=_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in MQ]}).replace('</','<\\/')
_mfq=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in MQ)
_MS=[('HMRC: Find out if and when you need to use Making Tax Digital for Income Tax (updated 26 Mar 2026)',MTD_FIND),
     ('HMRC: Work out your qualifying income for Making Tax Digital for Income Tax (updated 11 Sep 2026)',MTD_QI),
     ('HMRC: Send quarterly updates (Making Tax Digital for Income Tax)',MTD_Q),
     ('HMRC: Sign up for Making Tax Digital for Income Tax',MTD_SIGN),
     ('HMRC: Find out if you can get an exemption from Making Tax Digital for Income Tax',MTD_EX),
     ('HMRC: Clarification on abolition of the furnished holiday lettings tax regime', 'https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/clarification-on-abolition-of-the-furnished-holiday-lettings-tax-regime')]
_nopts=''.join(f'<option value="nation:{n["id"]}">{e(n["name"])}</option>' for n in d['nations'])
# Result alert (shown after checker runs); cta mtd-result
MTDALERT=('<div class="alertbox" id="mtd-result-alert" hidden><h2>Get an email when holiday-let tax and MTD rules change in <span id="mtd-an">your nation</span></h2>'
 '<p id="mtd-why">We track Making Tax Digital and holiday-let tax rules against HMRC and GOV.UK, and email you when one of them changes.</p>'
 '<p class="small">Plus one short weekly UK "what changed" email. Free. Unsubscribe any time.</p>'
 '<label for="mtd-rn">Your nation</label><select id="mtd-rn">'+_nopts+'</select>'
 +FORMX.replace('<form class="signup"','<form class="signup" id="mtd-rform" data-cta="mtd-result" data-area="nation:england" data-area-name="England"',1).replace('>Subscribe<','>Get free alerts<')+'</div>')
MTDJS=r'''<script>(function(){
var $=function(i){return document.getElementById(i)};
var TH={'2024-25':{t:50000,start:'6 April 2026',label:'2024 to 2025'},'2025-26':{t:30000,start:'6 April 2027',label:'2025 to 2026'},'2026-27':{t:20000,start:'6 April 2028',label:'2026 to 2027'}};
var WH={'england':'We track Making Tax Digital and holiday-let tax rules against HMRC and GOV.UK for England hosts, and email you when one of them changes.','scotland':'We track Making Tax Digital and holiday-let tax rules against HMRC and GOV.UK for Scotland hosts, and email you when one of them changes.','wales':'We track Making Tax Digital and holiday-let tax rules against HMRC and GOV.UK for Wales hosts, and email you when one of them changes.','northern-ireland':'We track Making Tax Digital and holiday-let tax rules against HMRC and GOV.UK for Northern Ireland hosts, and email you when one of them changes.'};
function money(n){return '£'+Math.round(n).toLocaleString('en-GB')}
function syncNat(){var F=$('mtd-rform'),S=$('mtd-rn');if(!F||!S)return;var o=S.options[S.selectedIndex],v=S.value,nm=o?o.textContent:'';F.setAttribute('data-area',v);F.setAttribute('data-area-name',nm);$('mtd-an').textContent=nm;var k=v.replace('nation:','');$('mtd-why').textContent=WH[k]||WH.england}
if($('mtd-rn')){$('mtd-rn').addEventListener('change',syncNat);syncNat()}
function run(){
 var y=$('mtd-year').value,p=parseFloat($('mtd-prop').value||'0'),s=parseFloat($('mtd-se').value||'0');
 if(isNaN(p)||isNaN(s)||p<0||s<0){$('mtd-rh').textContent='Check your numbers';$('mtd-rb').innerHTML='<p>Enter whole pounds of 0 or more for property and self-employment income.</p>';$('mtd-res').hidden=false;return}
 var q=p+s,info=TH[y],over=q>info.t,h,b;
 if(over){h='Likely start date: '+info.start;b='<p>Your estimated qualifying income for '+info.label+' is <b>'+money(q)+'</b> (property '+money(p)+' + self-employment '+money(s)+'). That is over the '+money(info.t)+' threshold, so HMRC says you need Making Tax Digital for Income Tax from <b>'+info.start+'</b>.</p>'}
 else{h='Below the '+info.label+' threshold';b='<p>Your estimated qualifying income for '+info.label+' is <b>'+money(q)+'</b>. That is not over '+money(info.t)+', so this year alone does not trigger a start on '+info.start+'. Check later tax years if your income rises, and use HMRC\'s official check tool.</p>'}
 b+='<p class="small"><b>Estimate from HMRC rules, not tax advice.</b> Qualifying income is gross turnover before expenses. Joint lets: count your share only. Confirm with <a href="'+'__FIND__'+'" rel="nofollow">HMRC\'s official check tool</a> and an accountant before acting.</p>';
 $('mtd-rh').textContent=h;$('mtd-rb').innerHTML=b;$('mtd-res').hidden=false;
 var A=$('mtd-result-alert'),S=document.querySelector('section.alertcta');if(A){A.hidden=false;if(S)S.hidden=true}
 try{localStorage.setItem('ukslr_mtd',JSON.stringify({y:y,p:p,s:s}))}catch(x){}
 try{gtag('event','mtd_check',{tax_year:y,over:over?'yes':'no'})}catch(x){}
}
$('mtd-go').addEventListener('click',run);
try{var L=JSON.parse(localStorage.getItem('ukslr_mtd')||'null');if(L){if(L.y)$('mtd-year').value=L.y;if(L.p!=null)$('mtd-prop').value=L.p;if(L.s!=null)$('mtd-se').value=L.s}}catch(x){}
})();</script>'''.replace('__FIND__',MTD_FIND)
_thr=''.join([
 f'<tr><td>2024 to 2025</td><td>Over £50,000</td><td>From 6 April 2026 (you can still sign up)</td><td><a href="{MTD_FIND}" rel="nofollow">source</a></td></tr>',
 f'<tr><td>2025 to 2026</td><td>Over £30,000</td><td>From 6 April 2027</td><td><a href="{MTD_FIND}" rel="nofollow">source</a></td></tr>',
 f'<tr><td>2026 to 2027</td><td>Over £20,000</td><td>From 6 April 2028</td><td><a href="{MTD_FIND}" rel="nofollow">source</a></td></tr>',
])
_qtr=''.join([
 '<tr><td>6 Apr to 5 Jul</td><td>7 August</td></tr>',
 '<tr><td>6 Apr to 5 Oct</td><td>7 November</td></tr>',
 '<tr><td>6 Apr to 5 Jan</td><td>7 February</td></tr>',
 '<tr><td>6 Apr to 5 Apr</td><td>7 May (next year)</td></tr>',
])
b=f'''<p class="lead">Making Tax Digital (MTD) for Income Tax means keeping digital records and sending quarterly updates through compatible software if your qualifying income is over HMRC\'s thresholds. Holiday-let income counts as property income. Here is who starts when, what counts, the quarterly dates, and a free qualifying-income checker.</p>
{TLDR([f'<b>Who:</b> sole traders and landlords registered for Self Assessment with self-employment and/or property income (<a href="{MTD_FIND}" rel="nofollow">HMRC</a>).',
 f'<b>Thresholds:</b> over £50,000 in 2024–25 → from 6 Apr 2026; over £30,000 in 2025–26 → from 6 Apr 2027; over £20,000 in 2026–27 → from 6 Apr 2028.',
 '<b>Holiday lets count:</b> gross holiday-let turnover is property income (FHL abolished Apr 2025) and forms part of qualifying income before expenses.',
 f'<b>Do now:</b> run the <a href="#mtd-checker">qualifying-income checker</a>, confirm with <a href="{MTD_FIND}" rel="nofollow">HMRC\'s check tool</a>, and <a href="#mtd-tax-alert">get MTD alerts</a>. Today (7 Nov) is the second quarterly update deadline for landlords already on MTD.'],
 title='In short: Making Tax Digital for holiday lets',sub='From HMRC GOV.UK guidance. Not tax advice.')}
{SCARDS([('2024–25 threshold','in','Over £50,000 → 6 Apr 2026','You can still sign up if you have not yet.','thresholds'),
 ('2025–26 threshold','coming','Over £30,000 → 6 Apr 2027','Next main wave for many holiday-let hosts.','thresholds'),
 ('2026–27 threshold','coming','Over £20,000 → 6 Apr 2028','Lower bar the year after.','thresholds'),
 ('Today','in','7 Nov quarterly update','Second update (6 Apr–5 Oct) due for landlords already on MTD; no late-update penalty points in 2026–27.','quarterly')])}
{TOC([('mtd-checker','Qualifying-income checker'),('thresholds','Thresholds'),('counts','What counts'),('quarterly','Quarterly update deadlines'),('hosts','What hosts should do now'),('mtd-tax-alert','Get MTD alerts'),('faq','Questions'),('sources','Sources')])}
<h2 id="mtd-checker">Qualifying-income checker</h2>
<div class="card"><form class="lvf" onsubmit="return false" id="mtd-form">
<label for="mtd-year">Tax year for the check</label>
<select id="mtd-year"><option value="2024-25">2024 to 2025 (threshold £50,000 → start 6 Apr 2026)</option><option value="2025-26" selected>2025 to 2026 (threshold £30,000 → start 6 Apr 2027)</option><option value="2026-27">2026 to 2027 (threshold £20,000 → start 6 Apr 2028)</option></select>
<label for="mtd-prop">Gross property income £ (before expenses; holiday lets + other property; your share only if joint)</label>
<input type="number" id="mtd-prop" min="0" step="1" inputmode="numeric" placeholder="e.g. 25000" value="">
<label for="mtd-se">Gross self-employment income £ (before expenses; 0 if none)</label>
<input type="number" id="mtd-se" min="0" step="1" inputmode="numeric" placeholder="e.g. 0" value="0">
<button type="button" id="mtd-go">Check my start date</button></form>
<div id="mtd-res" hidden aria-live="polite"><h3 id="mtd-rh"></h3><div id="mtd-rb"></div></div>
{MTDALERT}
<p class="small">Figures stay in your browser only (optional localStorage). Nothing is sent to this site until you subscribe. Official check: <a href="{MTD_FIND}" rel="nofollow">HMRC find out if and when</a>.</p></div>
{TOPICALERT('mtd-tax-alert','mtd-tax','Get an email when Making Tax Digital or holiday-let tax rules change',
 f'Today (7 Nov 2026) is the second quarterly update deadline for landlords already using Making Tax Digital. Next start waves are 6 April 2027 (£30,000 in 2025 to 2026) and 6 April 2028 (£20,000 in 2026 to 2027). We check <a href="{MTD_FIND}" rel="nofollow">HMRC</a> and GOV.UK and email you when something changes.',
 "Next MTD and tax dates we're watching",_rowdates(lambda r:r[1] in ('UK','England / Wales / NI')),
 [('','Choose your nation',False)]+[('nation:'+n['id'],n['name'],False) for n in d['nations']],'Your nation',
 'Pick the nation your let is in: you get UK tax and MTD changes plus rule changes for that nation.',
 'We have no upcoming MTD or tax dates logged right now. If HMRC or the government announces a change, we\'ll email you.')}
<h2 id="thresholds">1. Thresholds and start dates</h2>
<p>You need Making Tax Digital for Income Tax if you are a sole trader or landlord registered for Self Assessment, you get self-employment and/or property income, and your qualifying income is over the threshold for the relevant tax year (<a href="{MTD_FIND}" rel="nofollow">HMRC, updated 26 Mar 2026</a>).</p>
<div class="tw"><table><tr><th>Tax year</th><th>Qualifying income</th><th>Start using MTD</th><th>Official source</th></tr>{_thr}</table></div>
<ul class="tick"><li>Partnerships will need MTD later; HMRC has not set that timeline yet.</li>
<li>You still need a Self Assessment return for the tax year before you start MTD.</li>
<li>To sign up you must be registered for Self Assessment and have submitted a tax return in the last 2 years (<a href="{MTD_FIND}" rel="nofollow">HMRC</a>; <a href="{MTD_SIGN}" rel="nofollow">sign-up guidance</a>).</li></ul>
{CALLOUT(f'<p>Use our <a href="#mtd-checker">checker</a> for a quick estimate, then confirm with <a href="{MTD_FIND}" rel="nofollow">HMRC\'s official check tool</a> (it also covers exemptions).</p>')}
<h2 id="counts">2. What counts as qualifying income</h2>
<p>Qualifying income is total <b>gross</b> income from self-employment <b>and</b> property <b>before expenses</b> (turnover), not profit (<a href="{MTD_QI}" rel="nofollow">HMRC, updated 11 Sep 2026</a>).</p>
<ul class="tick"><li><b>Holiday-let income counts</b> as property income. The FHL regime was abolished from April 2025, so former furnished holiday lets are taxed as ordinary property income and still feed into this total. See <a href="holiday-let-tax-after-fhl-abolition.html">holiday let tax after the FHL abolition</a>.</li>
<li><b>Joint property:</b> count only your share (HMRC example: £50,000 income split 50/50 → £25,000 each).</li>
<li><b>Does not count:</b> PAYE employment, partnership profit share as an individual partner, dividends (including from your own company), State Pension, private pensions, REIT/PAIF income, qualifying care relief, and basis-period transition profits.</li>
<li>Income from a source you have ceased still counts if another self-employment or property source continues. If <b>all</b> self-employment and property sources ceased before 6 April 2026, you do not need MTD for Income Tax.</li>
<li>Property income with a short accounting period: you must annualise the figure yourself before comparing it with the threshold.</li></ul>
<h2 id="quarterly">3. Quarterly update deadlines</h2>
<p>Quarterly updates are summaries of your digital records sent by compatible software. They are not full tax returns (<a href="{MTD_Q}" rel="nofollow">HMRC</a>).</p>
<div class="tw"><table><tr><th>Standard period (tax year)</th><th>Update due by</th></tr>{_qtr}</table></div>
<p>If you use calendar periods (1 April to 31 March accounting), the same four deadlines apply: 7 August, 7 November, 7 February and 7 May.</p>
<ul class="tick"><li><b>2026 to 2027 tax year:</b> no penalty points for late quarterly updates. You still need to send the updates before your software tax return. Penalties for late Self Assessment returns still apply.</li>
<li><b>After 2026–27:</b> a late quarterly update can give a penalty point; four points lead to a £200 penalty.</li>
<li><b>7 November 2026</b> is the second quarterly update deadline (period 6 April to 5 October) for landlords already using MTD.</li></ul>
<p>See also the <a href="deadlines.html">UK short-let deadlines</a> page for Self Assessment and other host dates.</p>
<h2 id="hosts">4. What hosts should do now</h2>
<ul class="tick"><li>Work out your qualifying income for 2024–25, 2025–26 and 2026–27 with the <a href="#mtd-checker">checker</a>, then confirm on <a href="{MTD_FIND}" rel="nofollow">GOV.UK</a>.</li>
<li>If you are already in scope from 6 April 2026, send any outstanding quarterly updates through your software and note the 7 Nov / 7 Feb / 7 May deadlines.</li>
<li>If you start from 6 April 2027 or 2028, choose compatible software in good time and <a href="{MTD_SIGN}" rel="nofollow">sign up</a> when HMRC says you can.</li>
<li>Keep digital records of holiday-let income and expenses from the start of the tax year you join.</li>
<li>If you think you are digitally excluded or otherwise exempt, read <a href="{MTD_EX}" rel="nofollow">HMRC\'s exemption guidance</a> and apply before your start date. Exempt hosts still file a Self Assessment return.</li>
<li>Sign up below for alerts when MTD or holiday-let tax rules change.</li></ul>
<p><span class="tag">UNVERIFIED</span> We do not list named software products here. HMRC publishes a list of compatible software; check GOV.UK before buying.</p>
<h2 id="faq">Common questions</h2><div class="faq">{_mfq}</div>
<p class="small">More detail: <a href="holiday-let-tax-after-fhl-abolition">Holiday let tax after the FHL abolition</a> · <a href="deadlines">UK short-let deadlines</a> · <a href="occupancy-threshold-tracker">Occupancy threshold tracker</a> · <a href="guides">All guides</a>.</p>
<h2 id="sources">Official sources</h2>{SOURCES(_MS,'Show all official sources')}
<p class="small"><b>Not tax advice.</b> General information based on the HMRC and GOV.UK sources above, checked {_CHECKED}. Tax depends on your circumstances. Confirm with HMRC\'s tools and an accountant before acting. Free to cite with a link back. The UK Short-Let Rules team.</p>
{MTDJS}'''
page(f,t,b,desc=dsc,full_title='Making Tax Digital for holiday lets: thresholds and checker | UK Short-Let Rules',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{_mld}</script>',checked=_CHECKED)
