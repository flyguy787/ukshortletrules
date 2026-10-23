# 90-day UK short-let deadlines (re-verified 23 Oct 2026 against each official source).
DL=[
 ('2026-10-27','Scotland','East Lothian','Full council meeting considers visitor levy consultation findings and next steps','https://www.eastlothian.gov.uk/news/2026/council-asked-approve-independent-review-visitor-levy-plans'),
 ('2026-11-11','Scotland','Perth & Kinross','Visitor levy consultation closes','https://www.visitscotland.org/tourism-events-industry/visitor-levy'),
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
]
AHEAD=[('2027-03-31','Wales','All of Wales','Register your visitor accommodation with the Welsh Revenue Authority','https://www.gov.wales/visitor-levy-for-visitor-accommodation-providers-overview'),
 ('2027-04-01','Wales / Scotland','Cardiff and Aberdeen','Visitor levies start','https://www.gov.wales/check-if-local-council-charges-visitor-levy-wales')]
import datetime as _dt
_f=lambda s:_dt.date.fromisoformat(s).strftime('%a %-d %b %Y')
_r=lambda L:''.join(f'<tr><td><b>{_f(a)}</b></td><td>{e(c)}<br><span class="small">{e(n)}</span></td><td>{e(t)}</td><td><a href="{u}" rel="nofollow">source</a></td></tr>' for a,n,c,t,u in L)
page('deadlines.html','UK short-let deadlines: next 90 days',f'''<p class="lead">Every UK short-term let date we track from late October 2026 to the end of January 2027: levy start dates, payment deadlines, consultations closing and council decisions. Each date re-checked against its official source on 23 Oct 2026.</p>
<p><img src="deadlines-nov.png" alt="Card listing UK short-let deadlines from 27 Oct 2026 to 30 Jan 2027" width="540" height="675" style="max-width:100%;height:auto;border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,.12)"></p>
<p><a href="deadlines-nov.png" download>Download the card (PNG)</a> to share. Please link back to this page.</p>
<div class="tw"><table><tr><th>Date</th><th>Where</th><th>What</th><th>Official source</th></tr>{_r(DL)}</table></div>
<h2>Looking further ahead</h2><div class="tw"><table><tr><th>Date</th><th>Where</th><th>What</th><th>Official source</th></tr>{_r(AHEAD)}</table></div>
<p>Dates can move. Check the source before acting, and see the <a href="changes.html">changes log</a> for updates.</p>
<div class="box"><h2>Get a reminder when dates change</h2>{FORM}</div>''',desc='UK short-let deadlines for the next 90 days: Glasgow levy start, Edinburgh levy payment dates, Highland decision, consultations closing, with official sources.',full_title='UK short-let deadlines: next 90 days (Oct 2026 to Jan 2027) | UK Short-Let Rules')
# card HTML for the PNG (outside the site)
_card=''.join(f'<div class="r"><div class="d">{_dt.date.fromisoformat(a).strftime("%-d %b")}</div><div><b>{e(c)}</b> {e(t)}</div></div>' for a,n,c,t,u in DL)
import os
os.makedirs('/workspace/ukslr/design',exist_ok=True)
open('/workspace/ukslr/design/deadlines-card.html','w').write(f'''<!doctype html><meta charset="utf-8"><style>body{{margin:0;width:1080px;height:1350px;font:24px/1.25 system-ui,"DejaVu Sans",sans-serif;background:#123c5a;color:#fff}}.w{{padding:44px 64px 16px}}h1{{font-size:56px;margin:0 0 6px;line-height:1.1}}.s{{color:#f2a541;font-size:30px;font-weight:700;margin-bottom:20px}}.r{{display:flex;gap:24px;background:#fff;color:#1b2533;border-radius:14px;padding:10px 18px;margin:8px 0;align-items:center}}.d{{flex:0 0 120px;font-weight:800;color:#123c5a;font-size:25px;border-right:4px solid #f2a541}}.f{{padding:0 64px;font-size:21px;color:#d6e8f5}}.f b{{color:#f2a541;font-size:30px}}</style><div class="w"><h1>UK short-let deadlines</h1><div class="s">27 Oct 2026 to 30 Jan 2027</div>{_card}<div class="r" style="background:#f2a541"><div class="d" style="border-color:#123c5a">31 Mar</div><div><b>Wales</b> Register visitor accommodation with the WRA (Cardiff and Aberdeen levies start 1 Apr 2027)</div></div></div><div class="f">Sources: council, VisitScotland and GOV.WALES websites, checked 23 Oct 2026. Full list with links:<br><b>ukshortletrules.co.uk/deadlines</b></div>''')
