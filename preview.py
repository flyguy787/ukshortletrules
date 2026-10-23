# ---- Preview homepage (noindex, not in sitemap/nav, not linked) ----
_idx=open('index.html').read()
_tools=re.search(r'<h2>Free tools</h2>(<ul>.*?</ul>)',_idx).group(1)
NCOL={'england':'#c8102e','scotland':'#0065bd','wales':'#00843d','northern-ireland':'#6b4c9a'}
def _chips(n):return ''.join(f'<li><span class="k">{e(r["topic"])}</span><span class="s">{e(r["status"])}</span></li>' for r in n['rules'][:4])
pcards=''.join(f'<a class="nc" href="{n["id"]}.html" style="--nc:{NCOL[n["id"]]}"><h3>{n["name"]}</h3><p>{e(n["summary"])}</p><ul class="chips">{_chips(n)}</ul><span class="go">See {n["name"]} rules &rarr;</span></a>' for n in d['nations'])
pch=''.join(f'<li><time>{c["date"]}</time><span class="nt">{e(c["nation"])}</span><p>{e(c["text"])}</p></li>' for c in d['changes'][:4])
LOGO='<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#fff"/><path d="M7 17 17 8l10 9v9H7z" fill="#123c5a"/><rect x="14" y="19" width="6" height="7" rx="1" fill="#f2a541"/></svg>'
PCSS='''*{box-sizing:border-box}body{margin:0;font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;color:#1b2533;background:#f7f8fa}
a{color:#155a8a}:focus-visible{outline:3px solid #f2a541;outline-offset:2px}
.top{background:#123c5a;color:#fff}.bar{max-width:1120px;margin:auto;padding:.8rem 1.2rem;display:flex;flex-wrap:wrap;gap:.8rem 1.4rem;align-items:center;justify-content:space-between}
.wm{display:flex;gap:.6rem;align-items:center;color:#fff;text-decoration:none;font-weight:800;letter-spacing:-.01em;font-size:1.1rem}.wm small{display:block;font-weight:500;font-size:.75rem;color:#bcd6ea;letter-spacing:.04em;text-transform:uppercase}
.bar nav{display:flex;flex-wrap:wrap;gap:.2rem .9rem}.bar nav a{color:#d6e8f5;text-decoration:none;font-size:.92rem}.bar nav a:hover{color:#fff;text-decoration:underline}
.hero{background:linear-gradient(160deg,#123c5a 0%,#1d5880 100%);color:#fff;padding:3rem 1.2rem 3.5rem}.hin{max-width:1120px;margin:auto}
.hero h1{font-size:clamp(1.9rem,5vw,3.1rem);line-height:1.12;margin:0 0 .8rem;letter-spacing:-.02em;max-width:18ch}.hero p{font-size:1.15rem;color:#d6e8f5;max-width:60ch;margin:0 0 1.6rem}
.cta{display:inline-block;background:#f2a541;color:#1b2533;font-weight:700;padding:.85rem 1.3rem;border-radius:10px;text-decoration:none}.cta:hover{background:#ffb95c}.cta2{color:#fff;margin-left:1rem}
.trust{list-style:none;padding:0;margin:1.6rem 0 0;display:flex;flex-wrap:wrap;gap:.5rem 1.4rem;font-size:.9rem;color:#bcd6ea}.trust li:before{content:"\\2713  ";color:#f2a541;font-weight:700}
main{max-width:1120px;margin:auto;padding:0 1.2rem 2rem}
.ck{background:#fff;border-radius:16px;box-shadow:0 6px 24px #123c5a22;margin:-2rem 0 2rem;padding:1.4rem;display:grid;gap:1rem;border-top:5px solid #f2a541}
@media(min-width:760px){.ck{grid-template-columns:1.4fr 1fr;align-items:center}}.ck h2{margin:0 0 .3rem;font-size:1.35rem}.ck p{margin:0;color:#4a5668}.ck .cta{text-align:center}
h2.sec{font-size:1.5rem;letter-spacing:-.01em;margin:2.2rem 0 1rem}
.ngrid{display:grid;gap:1rem;grid-template-columns:1fr}@media(min-width:640px){.ngrid{grid-template-columns:1fr 1fr}}
.nc{display:flex;flex-direction:column;background:#fff;border-radius:14px;padding:1.2rem;color:inherit;text-decoration:none;border-top:6px solid var(--nc);box-shadow:0 1px 4px #0001}.nc:hover{box-shadow:0 6px 18px #0002}
.nc h3{margin:0 0 .3rem;font-size:1.3rem;color:var(--nc)}.nc p{margin:0 0 .8rem;font-size:.95rem;color:#3c4858}.go{margin-top:auto;font-weight:700;color:var(--nc);font-size:.92rem}
.chips{list-style:none;padding:0;margin:0 0 1rem;display:flex;flex-wrap:wrap;gap:.4rem}.chips li{font-size:.78rem;border:1px solid #dde3ea;border-radius:999px;overflow:hidden;display:flex}.chips .k{padding:.15rem .5rem;background:#f1f4f7}.chips .s{padding:.15rem .5rem;background:#fff4e3;color:#7a4a05;font-weight:600}
.chg{list-style:none;padding:0;margin:0;display:grid;gap:.8rem}@media(min-width:760px){.chg{grid-template-columns:1fr 1fr}}.chg li{background:#fff;border-radius:12px;padding:1rem;border-left:4px solid #f2a541}.chg time{font-weight:700;font-size:.85rem}.chg .nt{margin-left:.5rem;font-size:.75rem;background:#e7eff6;color:#123c5a;padding:.1rem .45rem;border-radius:999px}.chg p{margin:.4rem 0 0;font-size:.95rem}
.tools ul{background:#fff;border-radius:14px;padding:1rem 1rem 1rem 2.2rem;margin:0}.tools li{padding:.3rem 0}
.nl{background:#123c5a;color:#fff;border-radius:16px;padding:1.6rem;margin-top:2.4rem}.nl h2{margin:0 0 .3rem}.nl p{color:#d6e8f5}.nl .small{color:#bcd6ea}
.signup{display:flex;flex-wrap:wrap;gap:.5rem}.signup input[type=email]{flex:1 1 220px;padding:.8rem;font-size:1rem;border-radius:10px;border:0}.signup button{padding:.8rem 1.2rem;font-size:1rem;border:0;border-radius:10px;background:#f2a541;color:#1b2533;font-weight:700}.hp{position:absolute;left:-9999px}.msg{width:100%;margin:.3rem 0 0}
footer{text-align:center;font-size:.85rem;color:#556;padding:2rem 1.2rem}'''
_nav=re.search(r'<nav>.*?</nav>',_idx).group(0)
open('preview-home.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>UK Short-Let Rules Tracker (homepage preview)</title><link rel="canonical" href="{SITE}"><style>{PCSS}</style></head><body>
<header class="top"><div class="bar"><a class="wm" href="index.html">{LOGO}<span>UK Short-Let Rules<small>Tracker</small></span></a>{_nav}</div></header>
<section class="hero"><div class="hin"><h1>Every UK short-let rule, linked to its official source</h1><p>Licensing, planning, tax and safety rules for UK holiday-let and short-term-let hosts, with links to official sources.</p><a class="cta" href="checker.html">Do I need a licence? Check now</a><a class="cta2" href="councils.html">Browse {len(d["councils"])} councils</a><ul class="trust"><li>Every rule links to an official source</li><li>Last checked {C}</li><li>Free, independent, no tracking</li></ul></div></section>
<main><section class="ck" aria-labelledby="ckh"><div><h2 id="ckh">Do I need a licence or registration for my short let?</h2><p>Pick your nation and council for the key requirements, with source links. Free to <a href="embed.html">embed on your own site</a>.</p></div><a class="cta" href="checker.html">Open the licence checker</a></section>
<h2 class="sec">Rules by nation</h2><div class="ngrid">{pcards}</div>
<h2 class="sec">Latest changes</h2><ul class="chg">{pch}</ul><p><a href="changes.html">Full changes log &rarr;</a></p>
<section class="tools"><h2 class="sec">Free tools and guides</h2>{_tools}</section>
<section class="nl"><h2>Weekly "what changed" email</h2><p>One short, sourced email a week. Unsubscribe any time.</p>{FORM}</section></main>
<footer>Last checked {C}. General information only, not legal or tax advice. Always check the linked official source.<br>Want to reach UK hosts? <a href="sponsor.html">Sponsor the tracker</a></footer></body></html>''')
