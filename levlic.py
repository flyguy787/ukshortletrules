# ---- /uk-levy-and-licence-deadlines: every UK visitor levy + short-let licence deadline in one table ----
# Facts re-verified 6 Nov 2026 against each official source linked below. Built like deadlines.py / consult.py.
# Do not list Perth & Kinross (directory-only). Past consultation closes are not shown as open.
_LL_CHECKED='6 Nov 2026'
# Visitor levies: live / confirmed / proposed (Highland) / England Bill (not yet law). Columns match the draft.
_LL_LEVY=[
 # where, status_label, rate, start, who, sources[(label,url),...]
 ('Edinburgh (live)','5% of the accommodation-only cost, net of VAT, first 5 consecutive nights',
  'Stays from 24 Jul 2026 (bookings paid for before 1 Oct 2025 exempt)',
  'The accommodation provider is liable and remits the levy to the council; it chooses whether to pass the cost to guests',
  [('City of Edinburgh Council','https://www.edinburgh.gov.uk/visitorlevyinformation'),
   ('visitorlevy.scot','https://visitorlevy.scot/visitorlevy/pages/levy-scheme')]),
 ('Glasgow','5% of the overnight accommodation portion, net of VAT, whole stay',
  '25 Jan 2027 (bookings made from 1 Apr 2026 are liable)',
  'Charged on overnight stays; providers collect it and keep 1.5% for costs',
  [('Glasgow City Council','https://www.glasgow.gov.uk/article/14800/Accommodation-providers')]),
 ('Aberdeen','7% of overnight accommodation, whole stay',
  'Stays from 1 Apr 2027 (exempt only if booked and any payment made before 1 Oct 2026)',
  'Anyone staying in paid overnight accommodation; providers collect and report it, and may keep up to 2.5%',
  [('Aberdeen City Council','https://www.aberdeencity.gov.uk/Council-Services/business-and-investment/introducing-the-aberdeen-visitor-levy/information-for-businesses'),
   ('visitorlevy.scot','https://visitorlevy.scot/visitorlevy/pages/levy-scheme')]),
 ('Stirling','3% of the accommodation portion, charged before VAT (net of VAT)',
  'Stays from 14 Jun 2027, bookings made from 1 Jan 2027',
  'People using paid accommodation; Stirling council-tax residents and nights beyond 7 can claim a refund from the council after the stay',
  [('Stirling Council','https://www.stirling.gov.uk/about-the-council/stirling-visitor-levy-scheme/details-about-stirlings-visitor-levy-scheme/')]),
 ('West Dunbartonshire','5% before VAT, not on extras (parking, meals)',
  'Stays from 1 Jul 2027 (booked and paid before 1 Oct 2026 exempt)',
  'Paid overnight stays, including holiday and short-term lets; businesses below the VAT threshold are included; providers keep 1.5%',
  [('West Dunbartonshire Council','https://www.west-dunbarton.gov.uk/business/visitor-levy')]),
 ('Cardiff','£1.30 per person per night (75p per adult in tent pitches or shared hostel rooms)',
  'Stays from 1 Apr 2027 (bookings made from 28 Sep 2026 are liable)',
  'The accommodation provider pays; it can pass the cost to guests but is still responsible if they refuse',
  [('Welsh Government (rates)','https://www.gov.wales/visitor-levy-accommodation-providers-steps/how-much'),
   ('Welsh Government (dates)','https://www.gov.wales/check-if-local-council-charges-visitor-levy-wales')]),
 ('Highland (proposed)','Proposed £5 per room/area per night (hotels, B&amp;Bs, short-term lets); £2 (hostels, campsites, caravan parks); not Dec to Feb',
  'Council decides on 10 Dec 2026; then an 18-month lead-in before it could start. Consultation open to 30 Nov 2026',
  'Proposed; providers would keep 5% for costs',
  [('Highland Council (news)','https://www.highland.gov.uk/news/article/17462/highland-council-opens-statutory-public-consultation-on-a-tiered-fixed-amount-visitor-levy-proposal'),
   ('Highland Council (consultation)','https://www.highland.gov.uk/tourism-visitor-attractions/highland-visitor-levy/2')]),
 ('England (Overnight Visitor Levy Bill)','Percentage of accommodation cost, set locally if adopted; no rate or start yet',
  'Bill introduced 4 Nov 2026; not yet law. No levy applies anywhere in England under this Bill yet',
  'If enacted, mayors and Foundation Strategic Authority leaders could introduce a levy after local consultation; accommodation providers would account for and pay it',
  [('GOV.UK (MHCLG)','https://www.gov.uk/government/news/new-visitor-levy-powers-to-put-money-back-into-local-communities'),
   ('UK Parliament','https://bills.parliament.uk/bills/4320')]),
]
_LL_LIC=[
 ('Wales','Register with the Welsh Revenue Authority (free), even if your council has no levy',
  '31 Mar 2027',
  'Anyone taking bookings for overnight stays in visitor accommodation in Wales',
  [('Welsh Government','https://www.gov.wales/registering-visitor-accommodation-overview')]),
 ('England','Mandatory national registration scheme for short-term lets',
  'Expected to begin March 2027 (no exact date yet)',
  'Short-term let hosts in England',
  [('GOV.UK','https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations')]),
 ('Scotland','Short-term let licence from your council',
  'In force: needed before taking bookings (existing hosts\' deadline to apply was 1 Oct 2023)',
  'All short-term let accommodation, including holiday cottages, B&amp;Bs and rooms in a home',
  [('Scottish Government','https://www.gov.scot/publications/short-term-lets/')]),
 ('Northern Ireland','Tourism NI certificate: £40 per unit (min £40, max £350), valid 4 years',
  'In force: needed for all tourist accommodation',
  'All tourism and visitor accommodation',
  [('Tourism NI','https://www.tourismni.com/business-guidance/sector/accommodation/accommodation-getting-started/self-catering/overview/')]),
]
def _llsrc(S):
    return ', '.join(f'<a href="{e(u)}" rel="nofollow">{e(t)}</a>' for t,u in S)
_ll_lrows=''.join(
    f'<tr><td><b>{e(w)}</b></td><td>{e(r)}</td><td>{e(s)}</td><td>{e(who)}</td><td>{_llsrc(src)}</td></tr>'
    for w,r,s,who,src in _LL_LEVY)
_ll_irows=''.join(
    f'<tr><td><b>{e(w)}</b></td><td>{e(what)}</td><td>{e(dl)}</td><td>{e(who)}</td><td>{_llsrc(src)}</td></tr>'
    for w,what,dl,who,src in _LL_LIC)
# In-context alert (cta levy-licence-table). Nation picker (page spans all four nations); reasons are upcoming dates already on this page.
import datetime as _lldt
try:
    from zoneinfo import ZoneInfo as _llZ;_lltoday=_lldt.datetime.now(_llZ('Europe/London')).date()
except Exception:_lltoday=_lldt.date.today()
# Upcoming watchlist drawn from this page's own sourced dates (Europe/London, today or later)
_LL_WATCH=[
 ('2026-11-30','Scotland','Highland','Tiered fixed-amount visitor levy consultation closes','https://www.highland.gov.uk/tourism-visitor-attractions/highland-visitor-levy/2'),
 ('2026-12-10','Scotland','Highland','Council meeting could approve a visitor levy (then an 18-month lead-in)','https://www.highland.gov.uk/news/article/17462/highland-council-opens-statutory-public-consultation-on-a-tiered-fixed-amount-visitor-levy-proposal'),
 ('2027-01-25','Scotland','Glasgow','5% visitor levy starts (whole stay)','https://www.glasgow.gov.uk/article/14800/Accommodation-providers'),
 ('2027-03-31','Wales','All of Wales','Register visitor accommodation with the Welsh Revenue Authority','https://www.gov.wales/registering-visitor-accommodation-overview'),
 ('2027-03-31','England','All of England','Expected: national short-term let register begins (no exact date yet)','https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations'),
 ('2027-04-01','Wales','Cardiff','Visitor levy starts','https://www.gov.wales/check-if-local-council-charges-visitor-levy-wales'),
 ('2027-04-01','Scotland','Aberdeen','7% visitor levy starts','https://www.aberdeencity.gov.uk/Council-Services/business-and-investment/introducing-the-aberdeen-visitor-levy/information-for-businesses'),
 ('2027-06-14','Scotland','Stirling','3% visitor levy starts','https://www.stirling.gov.uk/about-the-council/stirling-visitor-levy-scheme/details-about-stirlings-visitor-levy-scheme/'),
 ('2027-07-01','Scotland','West Dunbartonshire','5% visitor levy starts','https://www.west-dunbarton.gov.uk/business/visitor-levy'),
]
_ll_up=[r for r in _LL_WATCH if _lldt.date.fromisoformat(r[0])>=_lltoday]
_ll_fx=lambda a,t:_lldt.date.fromisoformat(a).strftime('%B %Y')+' (expected)' if t.startswith('Expected') else _lldt.date.fromisoformat(a).strftime('%-d %b %Y')
_ll_keys=[_lldt.date.fromisoformat(r[0]).strftime('%-d %b %Y')+f': {i}' for i,r in enumerate(_ll_up)]
_ll_nx=[]
for k in NEXTD(_ll_keys):
    a,n,c,t,u=_ll_up[int(k.rsplit(': ',1)[1])]
    where=n if c.startswith('All of ') else c
    _ll_nx.append(f'<b>{_ll_fx(a,t)}, {e(where)}:</b> {e(t)} (<a href="{e(u)}" rel="nofollow">source</a>)')
_ll_opts=''.join(f'<option value="nation:{n["id"]}" data-name="{e(n["name"])}">{e(n["name"])}</option>' for n in d['nations'])
LLALERT=('<div class="alertbox alerttop" id="levy-licence-alert"><h2>Get an email before these levy and licence deadlines</h2>'
 +'<p>We check every rate and date on this page against its official source, and email you when a levy or licence deadline in your nation moves or a new one is announced.</p>'
 +((f'<p class="anxh"><b>Next deadlines we\'re watching:</b></p><ul class="anx">'+''.join(f'<li>{k}</li>' for k in _ll_nx)+'</ul>') if _ll_nx else '<p>We have no upcoming levy or licence deadlines logged right now. If a council or government announces one, we\'ll email you.</p>')
 +'<p class="small">Plus one short weekly UK "what changed" email. Free, no spam, unsubscribe any time.</p>'
 +FORMX.replace('<form class="signup"','<form class="signup pick" data-cta="levy-licence-table" aria-label="Get an email before these levy and licence deadlines"',1)
  .replace('<input type="email"','<label class="sr" for="levy-licence-alert-area">Your nation</label><select name="area" id="levy-licence-alert-area" required><option value="">Choose your nation</option>'+_ll_opts+'</select><input type="email"',1)
  .replace('>Subscribe<','>Get free alerts<')+'</div>')
# FAQ (sourced text only) + FAQPage JSON-LD
LLQ=[
 ('Which UK councils charge a visitor levy now?','Only Edinburgh charges a statutory visitor levy today: 5% of the accommodation-only cost, net of VAT, on the first 5 consecutive nights, for stays from 24 July 2026. Glasgow, Aberdeen, Stirling, West Dunbartonshire and Cardiff have confirmed start dates in 2027. Highland is still consulting (to 30 November 2026). England\'s Visitor Levy Bill was introduced on 4 November 2026 but is not yet law.'),
 ('Who pays the Edinburgh visitor levy — the guest or the host?','The accommodation provider is liable to the City of Edinburgh Council and remits the levy through visitorlevy.scot. Whether to pass the cost to guests is a business choice; the provider still owes the levy even if a guest does not pay it later.'),
 ('When do I need to register a holiday let in Wales?','If your accommodation is open for bookings before 1 April 2027, you must register with the Welsh Revenue Authority by 31 March 2027. Registration is free and applies even if your council never charges a visitor levy.'),
 ('When does short-term let registration start in England?','GOV.UK (updated 2 October 2026) says the mandatory national registration scheme for short-term lets in England is expected to begin in March 2027. No exact date, regulations, portal or fee have been published yet.'),
 ('Do I need a short-term let licence in Scotland?','Yes. Every short-term let in Scotland needs a licence from the local council before taking bookings. The scheme is already in force; the deadline for existing hosts to apply was 1 October 2023.'),
 ('Do holiday lets in Northern Ireland need a Tourism NI certificate?','Yes. Tourism law requires tourist accommodation, including self-catering, to hold a current Tourism NI certificate. The fee is £40 per unit (minimum £40, maximum £350) and the certificate is valid for four years.'),
 ('What is the England Overnight Visitor Levy Bill?','On 4 November 2026 the government introduced the Visitor Levy Bill in the House of Commons. It would let mayors and Foundation Strategic Authority leaders charge a percentage levy on overnight stays after local consultation. It is not yet law, and no rate or start date applies anywhere in England under the Bill.'),
 ('How do you keep these rates and dates up to date?','The UK Short-Let Rules team re-checks every claim on this page against the linked official source. Changes are logged in our changes log. Rates and dates can still move, so always check the source before acting.'),
]
LLQLD=json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in LLQ]}).replace('</','<\\/')
LLQH=('<h2 id="levy-licence-faq">Common questions</h2><div class="faq">'+''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in LLQ)+'</div>'
 +'<p class="small">More detail: <a href="deadlines">UK short-let deadlines</a> · <a href="uk-visitor-levy-map">UK visitor levy map</a> · <a href="levy-calculator">Visitor levy calculator</a> · <a href="wales-registration-checker">Wales registration checker</a> · <a href="england-short-term-let-rules-2027">England short-term let rules 2027</a> · <a href="scotland-short-term-let-licence-guide">Scotland licence guide</a> · <a href="northern-ireland-tourism-certificate-guide">Northern Ireland Tourism NI certificate</a> · <a href="consultations">Open consultations</a> · <a href="guides">Guides and free tools</a>.</p>'
 +'<p class="small">Checked '+_LL_CHECKED+'. Official sources: '
 +', '.join(f'<a href="{e(u)}" rel="nofollow">{e(t)}</a>' for t,u in [
  ('Edinburgh visitor levy information','https://www.edinburgh.gov.uk/visitorlevyinformation'),
  ('Glasgow accommodation providers','https://www.glasgow.gov.uk/article/14800/Accommodation-providers'),
  ('Aberdeen information for businesses','https://www.aberdeencity.gov.uk/Council-Services/business-and-investment/introducing-the-aberdeen-visitor-levy/information-for-businesses'),
  ('Stirling visitor levy scheme','https://www.stirling.gov.uk/about-the-council/stirling-visitor-levy-scheme/details-about-stirlings-visitor-levy-scheme/'),
  ('West Dunbartonshire visitor levy','https://www.west-dunbarton.gov.uk/business/visitor-levy'),
  ('Welsh Government: how much','https://www.gov.wales/visitor-levy-accommodation-providers-steps/how-much'),
  ('Welsh Government: councils charging','https://www.gov.wales/check-if-local-council-charges-visitor-levy-wales'),
  ('Highland consultation','https://www.highland.gov.uk/tourism-visitor-attractions/highland-visitor-levy/2'),
  ('GOV.UK Visitor Levy Bill news','https://www.gov.uk/government/news/new-visitor-levy-powers-to-put-money-back-into-local-communities'),
  ('WRA registering visitor accommodation','https://www.gov.wales/registering-visitor-accommodation-overview'),
  ('GOV.UK self-catering holiday homes in England','https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations'),
  ('Scottish Government short-term lets','https://www.gov.scot/publications/short-term-lets/'),
  ('Tourism NI self-catering overview','https://www.tourismni.com/business-guidance/sector/accommodation/accommodation-getting-started/self-catering/overview/'),
 ])+'.')
_ll_t='Every UK visitor levy and short-let licence deadline in one table'
_ll_ft='UK visitor levy and licence deadlines in one table | UK Short-Let Rules'
_ll_d='Every UK visitor levy rate, start date and who pays, plus Wales WRA, England register, Scotland licence and NI Tourism NI certificate deadlines. Official sources, checked 6 Nov 2026.'
_ll_body=(f'<p class="lead">Six councils have confirmed visitor levies, Highland votes in December, England\'s Visitor Levy Bill was introduced on 4 Nov 2026, and Wales and England both have registration deadlines in March 2027. Here is every date, rate and official source in one place for hosts, journalists and agents.</p>'
 +'<h2 id="visitor-levies">Visitor levies (tourist taxes)</h2>'
 +'<div class="tw"><table class="stk"><tr><th>Where</th><th>Rate</th><th>Start date</th><th>Who pays</th><th>Official source</th></tr>'+_ll_lrows+'</table></div>'
 +'<h2 id="licences">Licences and registration</h2>'
 +'<div class="tw"><table class="stk"><tr><th>Where</th><th>What</th><th>Deadline</th><th>Who</th><th>Official source</th></tr>'+_ll_irows+'</table></div>'
 +LLALERT
 +LLQH
 +'<p class="box"><b>Related tools:</b> <a href="deadlines">UK short-let deadlines</a> · <a href="uk-visitor-levy-map">UK visitor levy map</a> · <a href="levy-calculator">Visitor levy calculator</a> · <a href="wales-registration-checker">Wales registration checker</a> · <a href="consultations">Open consultations</a>.</p>'
 +'<p class="small">General information only, not legal or tax advice. Always check the official source. Free to cite or share with a link back to this page. The UK Short-Let Rules team.</p>')
page('uk-levy-and-licence-deadlines.html',_ll_t,_ll_body,desc=_ll_d,full_title=_ll_ft,
     head=OGT('uk-levy-and-licence-deadlines.html',_ll_t,_ll_d)+'<script type="application/ld+json">'+LLQLD+'</script>',
     checked=_LL_CHECKED)
