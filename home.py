# ---- Homepage (new design) ----
_idx=open('index.html').read()
_tools=re.search(r'<h2>Free tools</h2>(<ul>.*?</ul>)',_idx).group(1)
NCOL={'england':'#c8102e','scotland':'#0065bd','wales':'#00843d','northern-ireland':'#6b4c9a'}
def _chips(n):return ''.join(f'<li><span class="k">{e(r["topic"])}</span><span class="s">{e(r["status"])}</span></li>' for r in n['rules'][:4])
pcards=''.join(f'<a class="nc" href="{n["id"]}.html" style="--nc:{NCOL[n["id"]]}"><h3>{n["name"]}</h3><p>{e(n["summary"])}</p><ul class="chips">{_chips(n)}</ul><span class="go">See {n["name"]} rules &rarr;</span></a>' for n in d['nations'])
pch=''.join(f'<li><time>{c["date"]}</time><span class="nt">{e(c["nation"])}</span><p>{e(c["text"])}</p></li>' for c in [c for c in d['changes'] if not c.get('dir_only')][:4])
LOGO='<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#fff"/><path d="M7 17 17 8l10 9v9H7z" fill="#123c5a"/><rect x="14" y="19" width="6" height="7" rx="1" fill="#f2a541"/></svg>'

HERO=f'<section class="hero"><div class="hin"><h1>Every UK short-let rule, linked to its official source</h1><p>Licensing, planning, tax and safety rules for UK holiday-let and short-term-let hosts, with links to official sources.</p><a class="cta" href="checker.html">Do I need a licence? Check now</a><a class="cta2" href="councils.html">Browse {len(d["councils"])} councils</a><ul class="trust"><li>Every rule links to an official source</li><li>Last checked {C}</li><li>Free, independent, no ads</li></ul></div></section>'
# Homepage bottom signup: a reason to subscribe from facts already sourced on the site (same _nlitems lists as /newsletter: latest rule changes + next deadlines).
_hch,_hdl=_nlitems(2,6)
_hsrc=set(re.findall(r'href="([^"]+)"',_hch));_hdl=[x for x in _hdl if re.search(r'href="([^"]+)"',x).group(1) not in _hsrc][:3]  # don't repeat a change's own deadline
_hnf=FORMX.replace('<form class="signup"','<form class="signup" data-cta="home-weekly" aria-label="Get the weekly UK short-let rules email"',1).replace('>Subscribe<','>Get the weekly email<')
HNL=('<section class="nl hnl" id="weekly" aria-labelledby="weekly-h"><h2 id="weekly-h">Get the weekly UK short-let rules email</h2>'
 +'<p>One short email a week: what changed and what\'s coming for short-term and holiday lets in England, Scotland, Wales and Northern Ireland. Every item links to its official source.</p>'
 +(('<p class="anxh"><b>Recent rule changes:</b></p><ul class="anx">'+_hch+'</ul>') if _hch else '')
 +(('<p class="anxh"><b>Deadlines coming up:</b></p><ul class="anx hdl">'+''.join(_hdl)+'</ul>') if _hdl else '')
 +_hnf+'<p class="small">Free, no spam, unsubscribe any time. Want an email when your own council\'s rules change? <a href="#get-alerts">Pick your council for free alerts</a>. <a href="newsletter.html">More about the newsletter</a></p></section>')

# Homepage tools: top-5 tool cards + one card per nation (short link lists) + UK-wide extras collapsed (30 Oct retro: replace the 30-link list)
TOP5=[('checker.html','Do I need a licence?','3 questions: your nation, council and type of let.'),
 ('levy-calculator.html','Visitor levy calculator','Levy due on a booking, plus a guest message.'),
 ('uk-visitor-levy-map.html','Visitor levy map','Which councils charge, rates and start dates.'),
 ('deadlines.html','Deadlines: next 90 days','Every UK short-let date coming up.'),
 ('occupancy-threshold-tracker.html','Occupancy thresholds','Business rates or council tax? Count your nights.')]
NTOOLS={'england':[('england-short-term-let-rules-2027.html','What changes in 2027'),('england-holiday-let-planning-permission.html','Planning permission'),('england-second-homes-council-tax-premium.html','Second homes premium'),('holiday-let-fire-safety-england.html','Fire safety checklist'),('london-90-night-counter.html','London 90-night counter')],
 'scotland':[('scotland-short-term-let-licence-guide.html','How to get a licence'),('scotland-short-term-let-licence-fees.html','Licence fees, 32 councils'),('scotland-business-rates-checker.html','Business rates checker'),('scotland-licence-renewal-checker.html','Licence renewal checker'),('short-term-let-fire-safety-scotland.html','Fire safety checklist')],
 'wales':[('wales-registration-checker.html','WRA registration checker'),('wales-second-homes-council-tax-premium.html','Second homes premium'),('holiday-let-fire-safety-wales.html','Fire safety checklist'),('wales-visitor-accommodation-licensing.html','Licensing (2026 Act)')],
 'northern-ireland':[('northern-ireland-tourism-certificate-guide.html','Tourism NI certificate guide')]}
UKX=[('holiday-let-tax-after-fhl-abolition.html','Holiday let tax after the FHL abolition'),('holiday-let-insurance-uk.html','Do I need insurance for a holiday let?'),('buyer-due-diligence-checker.html','Buying a holiday let: due-diligence checker'),('embed.html','Embed the licence checker on your site'),('guides.html','All guides')]
TOOLCARDS=('<h3 class="tsub">Most used</h3><div class="tgrid">'+''.join(f'<a class="tcard" href="{u}"><b>{e(t)}</b><span>{e(x)}</span></a>' for u,t,x in TOP5)+'</div>'
 +'<h3 class="tsub">By nation</h3><div class="tgrid tn">'+''.join(f'<div class="tcard tnat" style="--nc:{NCOL[n["id"]]}"><b><a href="{n["id"]}.html">{e(n["name"])}</a></b><ul>'+''.join(f'<li><a href="{u}">{e(t)}</a></li>' for u,t in NTOOLS[n["id"]])+'</ul></div>' for n in d['nations'])+'</div>'
 +'<details class="more"><summary>More UK-wide tools and guides</summary><ul>'+''.join(f'<li><a href="{u}">{e(t)}</a></li>' for u,t in UKX)+'</ul></details>')
HB=PICK('home')+f'<section class="ckcard" aria-labelledby="ckh"><div><h2 id="ckh">Do I need a licence or registration for my short let?</h2><p>Three questions (nation, council, type of let) for a plain-English answer, the official source and your council page. Free to <a href="embed.html">embed on your own site</a>.</p></div><a class="cta" href="checker.html">Open the licence checker</a></section><h2 class="sec">Rules by nation</h2><div class="ngrid">{pcards}</div><h2 class="sec">Latest changes</h2><ul class="chg">{pch}</ul><p><a href="changes.html">Full changes log &rarr;</a></p><section class="tools"><h2 class="sec">Free tools and guides</h2>{TOOLCARDS}</section>{HNL}'
page('index.html','Current short-let rules across the UK',HB,head=HOME_OG,pre=HERO,noh1=True,full_title='UK Short-Let Rules Tracker: every UK short-let rule, linked to its official source',desc='Licensing, planning, tax and safety rules for UK holiday-let and short-term-let hosts in England, Scotland, Wales and Northern Ireland, with links to official sources.')
open('preview-home.html','w').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="robots" content="noindex"><link rel="canonical" href="{SITE}"><meta http-equiv="refresh" content="0; url=/"><title>Moved</title></head><body><p>This preview is now the homepage: <a href="/">go to the homepage</a>.</p></body></html>')
