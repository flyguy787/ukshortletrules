# Buyer due-diligence checker. Uses our council data (CX) + nation rules; postcode lookup via postcodes.io (fetch only, no script).
import json as _j
_NR={n['id']:{r['topic']:r for r in n['rules']} for n in d['nations']}
def _nr(nid,*ts):
    for t in ts:
        if t in _NR.get(nid,{}):r=_NR[nid][t];return [r['text'],r['sources']]
    return None
_BN={}
for n in d['nations']:
    nid=n['id']
    _BN[nid]=dict(name=n['name'],rates=_nr(nid,'Non-domestic rates thresholds','Business rates vs council tax','182-day rule (rates)','Rates'),
        reg=_nr(nid,'Registration (WRA)','Registration scheme','Certification'))
_BC=[]
for c in d['councils']:
    s=slug(c)
    if s not in CX or not c['verified']:continue
    x=CX[s];f=lambda k:[x[k][0].replace('../',''),x[k][1]]
    _BC.append(dict(n=c['name'],s=s,nat=c['nation'].lower().replace(' ','-'),r=c['rule'],src=c['source'],lic=f('lic'),ctrl=f('ctrl'),levy=f('levy')))
GEN=[('Mortgage lender consent','Mortgage terms normally require you to ask the lender for consent before running a business from a property. Ask your lender or broker whether short-term letting is allowed on the product you plan to use. We make no claims about any lender.',['https://www.mygov.scot/home-based-business/before-you-start','https://www.mygov.scot/landlord-responsibilities']),
 ('Insurance','You need cover that suits short-term letting: holiday let insurance, public liability and buildings and contents cover. In Scotland, valid buildings insurance and public liability insurance for each let are mandatory licence conditions.',['https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations','https://www.gov.scot/publications/short-term-lets-licensing-scheme-part-1-guidance-hosts-operators/pages/2/']),
 ('Lease, title deeds and owner consent','Check the title deeds (and the lease if the property is leasehold) for restrictions on running a business or letting, and get written consent where needed. In Scotland a licence application is refused without the consent of every owner.',['https://www.mygov.scot/home-based-business/before-you-start','https://www.gov.scot/publications/short-term-lets-licensing-scheme-part-1-guidance-hosts-operators/pages/2/']),
 ('Planning history','Ask your solicitor to confirm the property\'s lawful use and any planning permission or certificate for short-term letting, especially in a control area.',[]),
 ('Existing licence or registration','A licence or registration is usually personal to the operator or needs updating on a sale. Check with the council (Scotland) or the registration body before you rely on the seller\'s.',[])]
_opts=''.join(f'<option value="{c["s"]}">{e(c["n"])} ({e(c["nat"].replace("-"," ").title())})</option>' for c in sorted(_BC,key=lambda c:c['n']))
BJS='''<script>(function(){var C=__C__,N=__N__,G=__G__,$=function(i){return document.getElementById(i)};
function lk(s){return s&&s.length?' '+s.map(function(u){return '<a href="'+u+'" rel="nofollow">Source</a>'}).join(' '):''}
function nm(x){return x.toLowerCase().replace(/&/g,'and').replace(/^city of /,'').replace(/ city$/,'').replace(/[^a-z]/g,'')}
function sec(h,x){return x?'<div class="rc"><h3>'+h+'</h3><p>'+x[0]+lk(x[1])+'</p></div>':''}
function show(c){var n=N[c.nat]||{};$('br').innerHTML='<h2>'+c.n+'</h2><p class="lead">'+c.r+' <a href="'+c.src+'" rel="nofollow">Council source</a></p><div class="rcs">'+sec('Licence or registration',c.lic)+sec('Planning / control area',c.ctrl)+sec('Visitor levy',c.levy)+sec('Business rates or council tax (and second homes premium risk)',n.rates)+sec((n.name||'')+' registration or certification',n.reg)+'</div><p><a href="councils/'+c.s+'.html">Full '+c.n+' page</a> · <a href="occupancy-threshold-tracker.html">Occupancy threshold tracker</a></p><h2>Checks for every purchase</h2><div class="rcs">'+G.map(function(g){return sec(g[0],[g[1],g[2]])}).join('')+'</div><p class="small"><b>General information, not legal or financial advice.</b> Rules change: check the official sources and ask your solicitor. Data checked __D__.</p>';$('br').hidden=false;$('br').focus()}
$('bgo').addEventListener('click',function(){var v=$('bc').value;for(var i=0;i<C.length;i++)if(C[i].s==v)return show(C[i])});
$('bpgo').addEventListener('click',function(){var p=$('bp').value.replace(/\\s/g,'');$('bpm').textContent='Looking up...';
 fetch('https://api.postcodes.io/postcodes/'+encodeURIComponent(p)).then(function(r){return r.json()}).then(function(j){if(!j.result){$('bpm').textContent='Postcode not found. Pick the council instead.';return}
 var r=j.result,d=r.admin_district||'',k=nm(d),hit=null;
 for(var i=0;i<C.length;i++){if(nm(C[i].n)==k)hit=C[i]}
 if(!hit&&r.region=='London')for(var i=0;i<C.length;i++)if(C[i].n.indexOf('London')>=0)hit=C[i];
 if(hit){$('bpm').textContent=p.toUpperCase()+' is in '+d+'.';$('bc').value=hit.s;show(hit)}
 else{$('bpm').innerHTML=p.toUpperCase()+' is in '+d+' ('+(r.country||'')+'). We do not cover this council yet: see the <a href="'+((r.country||'').toLowerCase().replace(/ /g,'-'))+'.html">nation page</a> for national rules.'}
 }).catch(function(){$('bpm').textContent='Postcode lookup is unavailable. Pick the council instead.'})});
})();</script>'''.replace('__C__',_j.dumps(_BC)).replace('__N__',_j.dumps(_BN)).replace('__G__',_j.dumps(GEN)).replace('__D__',C)
page('buyer-due-diligence-checker.html','Buying a holiday let? Due-diligence checker',f'''<p class="lead">Before you buy a property to run as a short-term let, check the local rules: licence or registration, planning and control areas, visitor levy, business rates or council tax, plus the lender, insurance and lease checks every buyer should make. {len(_BC)} councils covered, checked {C}.</p>
<div class="card"><form class="lvf" onsubmit="return false"><label for="bp">Postcode</label><input id="bp" autocomplete="postal-code" placeholder="e.g. EH1 1YZ"><button type="button" id="bpgo">Look up postcode</button><p class="small" id="bpm" aria-live="polite">Postcode lookups use the free postcodes.io service (Office for National Statistics data). Only the postcode is sent.</p>
<label for="bc">Or choose a council</label><select id="bc">{_opts}</select><button type="button" id="bgo">Show checks</button></form></div>
<div id="br" hidden tabindex="-1" aria-live="polite"></div>
<noscript><p>This checker needs JavaScript. Browse the <a href="councils.html">council pages</a> instead.</p></noscript>{BJS}''',desc='Free due-diligence checker for buying a holiday let or short-term let in the UK: licence, planning, visitor levy, business rates and registration by council or postcode, plus lender, insurance and lease checks. Official sources.',full_title='Buying a holiday let? Free due-diligence checker by council or postcode | UK Short-Let Rules')
