// Email typo hint: suggest a fix for close misspellings of common domains or TLD typos. Never auto-corrects, never blocks.
var UKSLR_DOMAINS=['gmail.com','googlemail.com','hotmail.com','hotmail.co.uk','outlook.com','live.co.uk','yahoo.com','yahoo.co.uk','icloud.com','btinternet.com','aol.com','sky.com','virginmedia.com','me.com','msn.com'];
// Real providers that sit one or two edits from a listed domain: never "correct" these.
var UKSLR_VALID=['mail.com','ymail.com','gmx.com','gmx.co.uk','live.com','hotmail.fr','hotmail.de','hotmail.it','hotmail.es','outlook.co.uk','yahoo.fr','yahoo.de','yahoo.es','yahoo.it','yahoo.ie','mac.com','me.co.uk','sky.co.uk','bt.com','aim.com'];
function ukslrDist(a,b){var m=a.length,n=b.length,d=[],i,j;for(i=0;i<=m;i++){d[i]=[i];}for(j=0;j<=n;j++)d[0][j]=j;
  for(i=1;i<=m;i++)for(j=1;j<=n;j++){var c=a[i-1]===b[j-1]?0:1;d[i][j]=Math.min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+c);
    if(i>1&&j>1&&a[i-1]===b[j-2]&&a[i-2]===b[j-1])d[i][j]=Math.min(d[i][j],d[i-2][j-2]+1);}return d[m][n];}
function ukslrSuggest(email){
  email=String(email||'').trim();var at=email.lastIndexOf('@');if(at<1||at===email.length-1)return null;
  var name=email.slice(0,at),dom=email.slice(at+1).toLowerCase(),orig=dom;
  if(UKSLR_DOMAINS.indexOf(dom)>=0||UKSLR_VALID.indexOf(dom)>=0)return null;
  dom=dom.replace(/\.(con|cm|om)$/,'.com').replace(/\.co\.u$/,'.co.uk');
  if(UKSLR_DOMAINS.indexOf(dom)<0){var best=null,bd=9;
    for(var k=0;k<UKSLR_DOMAINS.length;k++){var c=UKSLR_DOMAINS[k],dd=ukslrDist(dom,c);
      // 1 edit anywhere; 2 edits only in the name part of a long domain with the same ending (e.g. gmaiil.com).
      var ok=dd===1||(dd===2&&dom.length>=9&&dom.slice(dom.indexOf('.'))===c.slice(c.indexOf('.')));
      if(ok&&dd<bd){best=c;bd=dd;}}
    if(best)dom=best;}
  return dom!==orig?name+'@'+dom:null;}
if(typeof module!=='undefined'&&module.exports)module.exports={ukslrSuggest:ukslrSuggest};
if(typeof document!=='undefined'){
function ukslrSrc(){try{return JSON.parse(sessionStorage.getItem('ukslr_src')||'{}')}catch(e){return {}}}
document.querySelectorAll('form.signup').forEach(function(f){
  if(f.dataset.bound)return;f.dataset.bound='1';
  var src=ukslrSrc();['utm_source','utm_medium','utm_campaign','referrer'].forEach(function(n){var i=document.createElement('input');i.type='hidden';i.name=n;i.value=src[n]||'';f.appendChild(i);});
  var em=f.querySelector('input[type=email]'),m0=f.querySelector('.msg');
  if(m0){m0.setAttribute('role','status');m0.setAttribute('aria-live','polite');}
  var hint=document.createElement('p');hint.className='ehint small';hint.setAttribute('aria-live','polite');
  if(m0)f.insertBefore(hint,m0);else f.appendChild(hint);
  function showHint(){var sg=em&&ukslrSuggest(em.value);hint.textContent='';if(!sg)return;
    var bt=document.createElement('button');bt.type='button';bt.className='sugg';bt.textContent=sg;
    bt.addEventListener('click',function(){em.value=sg;hint.textContent='';em.focus();});
    hint.appendChild(document.createTextNode('Did you mean '));hint.appendChild(bt);hint.appendChild(document.createTextNode('?'));}
  var ht;if(em){em.addEventListener('blur',showHint);em.addEventListener('input',function(){clearTimeout(ht);ht=setTimeout(showHint,600);});}
  var sel=f.querySelector('select[name=area]'),box=f.closest('.alertcta'),acn=box&&box.querySelector('.acn');
  function pick(){var o=sel&&sel.options[sel.selectedIndex];return o&&o.value?{area:o.value,name:o.getAttribute('data-name')||o.text}:null;}
  if(sel&&acn){var upd=function(){var p=pick();acn.textContent=p?(p.area.indexOf('nation:')===0?'all of '+p.name:p.name):'your council';};sel.addEventListener('change',upd);upd();}
  f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var m=f.querySelector('.msg'),b=f.querySelector('button:not(.sugg)'),url=f.dataset.endpoint;
    if(f.website.value){m.textContent='Thanks!';return;}
    if(!url){m.textContent='Signups open very soon. Thanks for your interest!';return;}
    var p=sel?pick():(f.dataset.area?{area:f.dataset.area,name:f.dataset.areaName||''}:null);
    if(sel&&!p){m.textContent='Please choose your council.';sel.focus();return;}
    var cta=f.dataset.cta||'newsletter';
    m.textContent='Subscribing...';b.disabled=true;
    fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.assign({email:f.email.value,website:f.website.value,utm_source:f.utm_source.value,utm_medium:f.utm_medium.value,utm_campaign:f.utm_campaign.value,referrer:f.referrer.value,cta:cta,page:location.pathname},p?{area:p.area,area_name:p.name}:{}))})
      .then(function(r){return r.json().catch(function(){return {ok:false};});})
      .then(function(j){
        if(j.ok){
          m.textContent=p?'Thanks! Alerts are on for '+(p.name||'your council')+', and you\'re on the weekly "what changed" email.':'Thanks! You\'re on the list for the weekly "what changed" email.';
          try{if(typeof window.gtag==='function'){gtag('event',p?'alert_signup':'newsletter_signup',{cta:cta,area:p?p.area:''});gtag('event','sign_up',{method:'email',cta:cta,council:p?p.area.replace(/^(council|nation):/,''):'',signup_type:p?'alert':'newsletter'});gtag('event','generate_lead',{form_location:cta,page_path:location.pathname,signup_type:p?'alert':'newsletter',area:p?p.area:''});}}catch(e){}
          f.email.value='';hint.textContent='';
        }
        else{m.textContent=j.error||'Sorry, something went wrong. Please try again.';}
      })
      .catch(function(){m.textContent='Sorry, something went wrong. Please try again.';})
      .finally(function(){b.disabled=false;});
  });
});
}
