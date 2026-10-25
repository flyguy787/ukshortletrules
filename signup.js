function ukslrSrc(){try{return JSON.parse(sessionStorage.getItem('ukslr_src')||'{}')}catch(e){return {}}}
document.querySelectorAll('form.signup').forEach(function(f){
  if(f.dataset.bound)return;f.dataset.bound='1';
  var src=ukslrSrc();['utm_source','utm_medium','utm_campaign','referrer'].forEach(function(n){var i=document.createElement('input');i.type='hidden';i.name=n;i.value=src[n]||'';f.appendChild(i);});
  var sel=f.querySelector('select[name=area]'),box=f.closest('.alertcta'),acn=box&&box.querySelector('.acn');
  function pick(){var o=sel&&sel.options[sel.selectedIndex];return o&&o.value?{area:o.value,name:o.getAttribute('data-name')||o.text}:null;}
  if(sel&&acn){var upd=function(){var p=pick();acn.textContent=p?(p.area.indexOf('nation:')===0?'all of '+p.name:p.name):'your council';};sel.addEventListener('change',upd);upd();}
  f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var m=f.querySelector('.msg'),b=f.querySelector('button'),url=f.dataset.endpoint;
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
          try{if(window.gtag)gtag('event',p?'alert_signup':'newsletter_signup',{cta:cta,area:p?p.area:''});}catch(e){}
          f.email.value='';
        }
        else{m.textContent=j.error||'Sorry, something went wrong. Please try again.';}
      })
      .catch(function(){m.textContent='Sorry, something went wrong. Please try again.';})
      .finally(function(){b.disabled=false;});
  });
});
