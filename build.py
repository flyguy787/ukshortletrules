import json,html
d=json.load(open('data.json'));e=html.escape;C=d['checked']
nav='<nav><a href="index.html">Home</a>'+''.join(f'<a href="{n["id"]}.html">{n["name"]}</a>' for n in d['nations'])+'<a href="councils.html">Councils</a><a href="changes.html">Changes</a><a href="newsletter.html">Newsletter</a></nav>'
def page(f,t,b):
    open(f,'w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(t)} | UK Short-Let Rules Tracker</title><link rel="stylesheet" href="style.css"></head><body><header><a class="brand" href="index.html">UK Short-Let Rules Tracker</a>{nav}</header><main><h1>{e(t)}</h1>{b}</main><aside class="sponsor">Sponsor this page: reach UK hosts. <a href="sponsor.html">Find out more</a></aside><footer>Last checked {C}. General information only, not legal or tax advice. Always check the linked official source.</footer></body></html>''')
src=lambda s:' '.join(f'<a href="{e(u)}" rel="nofollow">source</a>' for u in s) or '<em>no source yet</em>'
cards=''.join(f'<a class="card" href="{n["id"]}.html"><h2>{n["name"]}</h2><p>{e(n["summary"])}</p></a>' for n in d['nations'])
latest=''.join(f'<li><b>{c["date"]}</b> [{c["nation"]}] {e(c["text"])}</li>' for c in d['changes'][:4])
page('index.html','Current short-let rules across the UK',f'<p class="lead">Licensing, planning, tax and safety rules for UK holiday-let and short-term-let hosts, with links to official sources.</p><div class="grid">{cards}</div><h2>Latest changes</h2><ul>{latest}</ul><p><a href="changes.html">Full changes log</a> · <a href="newsletter.html">Get the weekly "what changed" email</a></p>')
for n in d['nations']:
    rows=''.join(f'<tr><td>{e(r["topic"])}</td><td><span class="tag{" warn" if "UNVERIFIED" in r["status"] else ""}">{e(r["status"])}</span></td><td>{e(r["text"])}</td><td>{src(r["sources"])}</td></tr>' for r in n['rules'])
    page(n['id']+'.html',n['name'],f'<p class="lead">{e(n["summary"])}</p><div class="tw"><table><tr><th>Topic</th><th>Status</th><th>Rule</th><th>Official source</th></tr>{rows}</table></div>')
rows=''.join(f'<tr><td>{e(c["name"])}</td><td>{c["nation"]}</td><td>{e(c["rule"])}</td><td>{"✔" if c["verified"] else "<span class=\"tag warn\">unverified</span>"}</td><td>{src([c["source"]] if c["source"] else [])}</td></tr>' for c in d['councils'])
page('councils.html','Councils with notable local rules',f'<div class="tw"><table><tr><th>Council</th><th>Nation</th><th>Rule</th><th>Verified</th><th>Source</th></tr>{rows}</table></div>')
rows=''.join(f'<tr><td>{c["date"]}</td><td>{c["nation"]}</td><td>{e(c["text"])}</td><td>{src([c["source"]])}</td></tr>' for c in d['changes'])
page('changes.html','Changes log',f'<div class="tw"><table><tr><th>Date</th><th>Nation</th><th>Change</th><th>Source</th></tr>{rows}</table></div>')
page('newsletter.html','Weekly "what changed" newsletter','<p>One short email every week: what changed, what\'s coming, and deadlines.</p><form onsubmit="alert(\'Signup not live yet. Thanks!\');return false"><input type="email" placeholder="you@example.com" required><button>Notify me</button></form><p class="small">Placeholder: no data is collected yet.</p>')
page('sponsor.html','Sponsor this page','<p>Reach UK short-let hosts who are actively checking compliance. Sponsorships are available for insurers, accountants, channel managers and safety providers. Each page can carry one clearly labelled sponsor. Sponsors never affect the content.</p><p class="small">Placeholder: contact details coming soon.</p>')
