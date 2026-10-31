# ---- Scotland short-term let licence fee finder (all 32 councils), built only from the sourced council-page fee text ----
import datetime as _fd
_fdt=_fd.date.fromisoformat(C).strftime('%-d %b %Y')
_fs=sorted([c for c in d['councils'] if c['nation']=='Scotland' and c['verified'] and slug(c) in CX],key=lambda c:c['name'].replace('City of ',''))
_NS=('Licence fees: not summarised','Licence fees: see','Not shown','Not summarised')
def _fok(t):return not t.strip().startswith(_NS)
_frows='';_fjs={}
for c in _fs:
    sl=slug(c);fx=CX[sl]['fees'];ok=_fok(fx[0])
    _fjs[sl]=dict(n=c['name'],f=fx[0],s=fx[1],ok=ok)
    _frows+=f'<tr id="fee-{sl}"><td><a href="councils/{sl}.html">{e(c["name"])}</a></td><td>{fx[0] if ok else "<span class=\"tag warn\">Check the council</span> "+fx[0]}</td><td>{src(fx[1])}</td></tr>'
_nok=sum(1 for v in _fjs.values() if v['ok'])
_fopts=''.join(f'<option value="{sl}">{e(v["n"])}</option>' for sl,v in _fjs.items())
_fdata=json.dumps(_fjs).replace('</','<\\/')
_fq=[('How much does a short-term let licence cost in Scotland?',f'There is no single national fee. Each of the 32 Scottish councils sets its own short-term let licence fee, usually by type of let (secondary letting, home letting or home sharing) and by number of guests or bedrooms, and many charge differently for new licences and renewals. This page lists the fee each council publishes, with its official source. We have a fee summary for {_nok} of the 32 councils; for the rest, check the council directly.'),
 ('Do I pay a different fee for secondary letting and home sharing?','In most councils, yes. Secondary letting (letting a property you do not live in) usually costs more than home letting or home sharing. Some councils, such as Angus and North Lanarkshire, charge the same fee for every type of licence. Check your council\'s row below.'),
 ('Is a renewal cheaper than a new licence?','It depends on the council. Some charge the same for new and renewal applications, and others, such as South Ayrshire, North Ayrshire and East Ayrshire, charge less for a renewal. Check your council\'s row and its official source.')]
_fld=json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in _fq]}).replace('</','<\\/')
_fb=f'''<p class="lead">Every Scottish council sets its own short-term let licence fee. Pick your council to see the fee it publishes, or compare all 32 in the table. Each fee links to the council's official source.</p>
<div class="box"><label for="feec"><b>Your council</b></label><br><select id="feec"><option value="">Choose a council…</option>{_fopts}</select><div id="feer" role="status" aria-live="polite"></div></div>
<p class="small">Fees as published by each council and summarised on our council pages, last checked up to {_fdt}. Councils usually review fees every April, so always confirm with the official source before you apply. General information only, not legal advice. Where we could not read a council's fee table, the row says <b>Check the council</b>.</p>
<h2>Short-term let licence fees by council</h2><div class="tw"><table class="stk"><tr><th>Council</th><th>Fees (as published)</th><th>Official source</th></tr>{_frows}</table></div>
<h2>Quick answers</h2>'''+''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in _fq)+'''
<h2>Related</h2><ul><li><a href="scotland-short-term-let-licence-guide.html">How to get a short-term let licence: steps and checklist</a></li><li><a href="scotland-licence-renewal-checker.html">Licence renewal checker</a></li><li><a href="checker.html">Do I need a licence? Free checker</a></li><li><a href="scotland.html">All Scotland short-let rules</a></li></ul>
<script>(function(){var D='''+_fdata+''',s=document.getElementById('feec'),r=document.getElementById('feer');function a(u){var x=document.createElement('a');x.href=u;x.rel='nofollow';x.textContent='official source';return x}s.addEventListener('change',function(){var v=D[s.value];r.innerHTML='';if(!v)return;var h=document.createElement('h3');h.textContent=v.n+': short-term let licence fees';var p=document.createElement('p');p.innerHTML=(v.ok?'':'<b>Check the council.</b> ')+v.f;var q=document.createElement('p');q.className='small';q.append('Source: ');v.s.forEach(function(u,i){if(i)q.append(' · ');q.append(a(u))});q.append(' · ');var c=document.createElement('a');c.href='councils/'+s.value;c.textContent='Full '+v.n+' rules';q.append(c);var t=document.createElement('p');t.innerHTML='<a href="councils/'+s.value+'#get-alerts">Get free alerts when '+v.n.replace(/&/g,'&amp;')+' changes its fees or rules</a>';r.append(h,p,q,t);try{gtag('event','fee_lookup',{council:s.value})}catch(e){}})})();</script>'''
page('scotland-short-term-let-licence-fees.html','Short-term let licence fees in Scotland: all 32 councils',_fb,desc=f'Compare short-term let licence fees across all 32 Scottish councils: secondary letting, home letting and home sharing, new and renewal, with each council\'s official source. Checked {_fdt}.',full_title='Scotland short-term let licence fees by council (all 32) | UK Short-Let Rules Tracker',head=f'<script type="application/ld+json">{_fld}</script>')
print('fee finder councils',len(_fjs),'with fees',_nok)
