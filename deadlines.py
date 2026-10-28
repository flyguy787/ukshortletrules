# UK short-let deadlines (re-verified 28 Oct 2026 against each official source). Rows whose date has passed
# (Europe/London) are hidden from the tables and the card at build time (_up); NEXTD does the same for the alert lists.
DL=[
 ('2026-10-30','Wales','All of Wales','Extended deadline (11:59pm) for the Welsh Government consultation on the 182-day self-catering local tax rule and proposed exemptions','https://www.gov.wales/classification-self-catering-properties-local-tax-purposes'),
 ('2026-10-31','UK','All of UK','Paper Self Assessment tax return for 2025 to 2026 (including holiday-let income) must reach HMRC by 11:59pm; online returns are due 31 Jan 2027','https://www.gov.uk/self-assessment-tax-returns/deadlines'),
 ('2026-11-07','UK','All of UK','Making Tax Digital for Income Tax: second quarterly update due (6 Apr to 5 Oct) for landlords already using it; no penalty points for late updates in 2026 to 2027','https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates'),
 ('2026-11-13','Scotland','Edinburgh','Last day to pay the levy for stays 24 Jul to 30 Sep 2026 (return due by 30 Oct)','https://www.edinburgh.gov.uk/visitorlevyinformation'),
 ('2026-11-15','Scotland','Argyll & Bute','Mull and Iona short-term let control area consultation closes','https://www.argyll-bute.gov.uk/my-community/community-planning/consultations/consultation/proposed-short-term-let-control-area'),
 ('2026-11-16','Northern Ireland','Belfast','Consultation on short-term let planning guidance closes','https://www.belfastcity.gov.uk/news/public-consultation-launched-looking-at-planning-g'),
 ('2026-11-25','Scotland','Falkirk','Visitor levy consultation closes','https://www.visitscotland.org/tourism-events-industry/visitor-levy'),
 ('2026-11-27','Scotland','Dundee','Visitor levy consultation closes','https://www.visitscotland.org/tourism-events-industry/visitor-levy'),
 ('2026-11-30','Scotland','Highland','Visitor levy consultation closes','https://www.visitscotland.org/tourism-events-industry/visitor-levy'),
 ('2026-12-10','Scotland','Highland','Council meeting could approve a visitor levy (then an 18-month lead-in)','https://www.highland.gov.uk/news/article/17462/highland-council-opens-statutory-public-consultation-on-a-tiered-fixed-amount-visitor-levy-proposal'),
 ('2027-01-01','Scotland','Stirling','Bookings made from today are liable to the 3% levy (stays from 14 Jun 2027)','https://www.stirling.gov.uk/about-the-council/stirling-visitor-levy-scheme/details-about-stirlings-visitor-levy-scheme/'),
 ('2027-01-25','Scotland','Glasgow','5% visitor levy starts (whole stay)','https://www.glasgow.gov.uk/article/14800/Accommodation-providers'),
 ('2027-01-30','Scotland','Edinburgh','Levy return due for stays 1 Oct to 31 Dec 2026 (pay by 13 Feb)','https://www.edinburgh.gov.uk/visitorlevyinformation'),
 ('2027-01-31','UK','All of UK','Online Self Assessment tax return for 2025 to 2026 due by 11:59pm, and any tax owed must be paid','https://www.gov.uk/self-assessment-tax-returns/deadlines'),
]
AHEAD=[('2027-02-13','Scotland','Edinburgh','Last day to pay the levy for stays 1 Oct to 31 Dec 2026','https://www.edinburgh.gov.uk/visitorlevyinformation'),
 ('2027-03-31','England','All of England','Expected: GOV.UK says the national short-term let register is expected to begin in March 2027 (no exact date, regulations or portal published yet)','https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations'),
 ('2027-03-31','Wales','All of Wales','Register your visitor accommodation with the Welsh Revenue Authority','https://www.gov.wales/visitor-levy-for-visitor-accommodation-providers-overview'),
 ('2027-04-01','Wales','Cardiff','Visitor levy starts','https://www.gov.wales/check-if-local-council-charges-visitor-levy-wales'),
 ('2027-04-01','Scotland','Aberdeen','7% visitor levy starts (every night of the stay)','https://www.aberdeencity.gov.uk/Council-Services/business-and-investment/introducing-the-aberdeen-visitor-levy'),
 ('2027-04-01','England','Stratford-on-Avon','100% council tax premium on second homes starts (double bill)','https://www.stratford.gov.uk/news/index.cfm/current/1/item/138732'),
 ('2027-04-01','England','Cherwell','100% council tax premium on second homes starts (double bill)','https://www.cherwell.gov.uk/info/236/discounts-and-exemptions/1419/council-tax-second-homes-premium-policy-2027-2028'),
 ('2027-04-06','UK','All of UK','Making Tax Digital for Income Tax applies if your self-employment and property income was over £30,000 in 2025 to 2026','https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax'),
 ('2027-04-06','England / NI','England and Northern Ireland','New property income tax rates: 22% basic, 42% higher, 47% additional (finance cost relief at 22%)','https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-dividend-income/changes-to-tax-rates-for-property-savings-dividend-income'),
 ('2027-04-30','Scotland','Edinburgh','Levy return due for stays 1 Jan to 31 Mar 2027 (pay by 14 May)','https://www.edinburgh.gov.uk/visitorlevyinformation'),
 ('2027-06-14','Scotland','Stirling','3% visitor levy starts (Stirling residents and nights beyond 7 refunded)','https://www.stirling.gov.uk/about-the-council/stirling-visitor-levy-scheme/details-about-stirlings-visitor-levy-scheme/'),
 ('2027-07-01','Scotland','West Dunbartonshire','5% visitor levy starts (whole stay)','https://www.west-dunbarton.gov.uk/business/visitor-levy'),
]
import datetime as _dt
try:
    from zoneinfo import ZoneInfo as _Z;_dtoday=_dt.datetime.now(_Z('Europe/London')).date()
except Exception:_dtoday=_dt.date.today()
_up=lambda L:[r for r in L if _dt.date.fromisoformat(r[0])>=_dtoday]
_f=lambda s:_dt.date.fromisoformat(s).strftime('%a %-d %b %Y')
# 'Expected:' rows have no exact day at source: show the month, marked expected (here and in the alert/newsletter lists)
_fx=lambda a,t,F=_f:_dt.date.fromisoformat(a).strftime('%B %Y')+' (expected)' if t.startswith('Expected') else F(a)
_r=lambda L:''.join(f'<tr><td><b>{_fx(a,t)}</b></td><td>{e(c)}<br><span class="small">{e(n)}</span></td><td>{e(t)}</td><td><a href="{u}" rel="nofollow">source</a></td></tr>' for a,n,c,t,u in L)
# In-context alert box (same form/endpoint/signup.js as ALERT_TOP/WALERT). Reason to subscribe: the next 3 upcoming dates
# from this page's own sourced DL/AHEAD rows (NEXTD: today or later, Europe/London). The page covers several nations, so the
# visitor picks one (values nation:<id>, the same encoding PICK uses); cta 'deadlines'; id deadlines-alert (sitewide #get-alerts stays unique).
_dlr=DL+AHEAD;_dlk=[_dt.date.fromisoformat(r[0]).strftime('%-d %b %Y')+f': {i}' for i,r in enumerate(_dlr)]
_dln=[(lambda a,n,c,t,u:f'<b>{_fx(a,t,lambda x:_dt.date.fromisoformat(x).strftime("%-d %b %Y"))}, {e(n if c=="All of "+n else c)}:</b> {e(t)} (<a href="{e(u)}" rel="nofollow">source</a>)')(*_dlr[int(k.rsplit(": ",1)[1])]) for k in NEXTD(_dlk)]
_dlo=''.join(f'<option value="nation:{n["id"]}" data-name="{e(n["name"])}">{e(n["name"])}</option>' for n in d['nations'])
DLALERT=('<div class="alertbox alerttop" id="deadlines-alert"><h2>Get an email before these short-let deadlines</h2><p>We check every date on this page against its official source, and email you when a deadline in your nation moves or a new one is announced.</p>'
 +((f'<p class="anxh"><b>Next deadlines we\'re watching:</b></p><ul class="anx">'+''.join(f'<li>{k}</li>' for k in _dln)+'</ul>') if _dln else '<p>We have no upcoming deadlines logged right now. If a council or government announces one, we\'ll email you.</p>')
 +'<p class="small">Plus one short weekly UK "what changed" email. Free, no spam, unsubscribe any time.</p>'
 +FORMX.replace('<form class="signup"','<form class="signup pick" data-cta="deadlines" aria-label="Get an email before these short-let deadlines"',1).replace('<input type="email"','<label class="sr" for="deadlines-alert-area">Your nation</label><select name="area" id="deadlines-alert-area" required><option value="">Choose your nation</option>'+_dlo+'</select><input type="email"',1).replace('>Subscribe<','>Get free alerts<')+'</div>')
_cu=_up(DL);_cr=(_dt.date.fromisoformat(_cu[0][0]).strftime('%-d %b %Y')+' to '+_dt.date.fromisoformat(_cu[-1][0]).strftime('%-d %b %Y')) if _cu else 'none upcoming'
page('deadlines.html','UK short-let deadlines: next 90 days',f'''<p class="lead">Every UK short-term let and holiday let date we track for the next 90 days, then the bigger dates to July 2027: levy start dates, levy returns and payments, Self Assessment and Making Tax Digital deadlines, council tax premiums, consultations closing and council decisions, in all four nations. Each date re-checked against its official source on 28 Oct 2026; past dates drop off automatically.</p>
<p><img src="deadlines-nov.png" alt="Card listing UK short-let deadlines from {_cr}" width="540" height="675" style="max-width:100%;height:auto;border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,.12)"></p>
<p><a href="deadlines-nov.png" download>Download the card (PNG)</a> to share. Please link back to this page.</p>
<div class="tw"><table><tr><th>Date</th><th>Where</th><th>What</th><th>Official source</th></tr>{_r(_up(DL))}</table></div>
<h2>Looking further ahead</h2><div class="tw"><table><tr><th>Date</th><th>Where</th><th>What</th><th>Official source</th></tr>{_r(_up(AHEAD))}</table></div>
<p>Dates can move. Check the source before acting, and see the <a href="changes.html">changes log</a> for updates.</p>
{DLALERT}''',desc='UK short-let deadlines: Self Assessment, Edinburgh and Glasgow levy dates, consultations closing, then Aberdeen, Cardiff and Stirling levies, England register and premiums to July 2027. Official sources.',full_title='UK short-let deadlines: next 90 days and 2027 dates | UK Short-Let Rules')
# card HTML for the PNG (outside the site)
_card=''.join(f'<div class="r"><div class="d">{_dt.date.fromisoformat(a).strftime("%-d %b")}</div><div><b>{e(c)}</b> {e(t)}</div></div>' for a,n,c,t,u in _up(DL))
import os
os.makedirs('/workspace/ukslr/design',exist_ok=True)
open('/workspace/ukslr/design/deadlines-card.html','w').write(f'''<!doctype html><meta charset="utf-8"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><style>body{{margin:0;width:1080px;height:1350px;font:21px/1.22 system-ui,"DejaVu Sans",sans-serif;background:#123c5a;color:#fff}}.w{{padding:36px 56px 12px}}h1{{font-size:52px;margin:0 0 4px;line-height:1.1}}.s{{color:#f2a541;font-size:30px;font-weight:700;margin-bottom:14px}}.r{{display:flex;gap:24px;background:#fff;color:#1b2533;border-radius:12px;padding:7px 16px;margin:6px 0;align-items:center}}.d{{flex:0 0 120px;font-weight:800;color:#123c5a;font-size:23px;border-right:4px solid #f2a541}}.f{{padding:0 64px;font-size:21px;color:#d6e8f5}}.f b{{color:#f2a541;font-size:30px}}</style><div class="w"><h1>UK short-let deadlines</h1><div class="s">{_cr}</div>{_card}<div class="r" style="background:#f2a541"><div class="d" style="border-color:#123c5a">31 Mar</div><div><b>Wales</b> Register visitor accommodation with the WRA (Cardiff and Aberdeen levies start 1 Apr 2027)</div></div></div><div class="f">Sources: council, VisitScotland, GOV.UK and GOV.WALES websites, checked 28 Oct 2026. Full list with links:<br><b>ukshortletrules.co.uk/deadlines</b></div>''')
