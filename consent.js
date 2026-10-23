(function(){
var K='ukslr_consent',b=document.getElementById('ckb');
function set(v){try{localStorage.setItem(K,v)}catch(e){}if(v==='granted')gtag('consent','update',{analytics_storage:'granted'});else gtag('consent','update',{analytics_storage:'denied'});hide()}
function hide(){if(b){b.hidden=true;document.body.classList.remove('ckb-on')}}
function show(){if(b){b.hidden=false;document.body.classList.add('ckb-on')}}
var s=null;try{s=localStorage.getItem(K)}catch(e){}
if(!s)show();
if(b){b.querySelector('.ckb-a').addEventListener('click',function(){set('granted')});b.querySelector('.ckb-r').addEventListener('click',function(){set('denied')})}
document.querySelectorAll('.ck-open').forEach(function(a){a.addEventListener('click',function(ev){ev.preventDefault();show();var x=b&&b.querySelector('.ckb-a');if(x)x.focus()})});
function ev(n,p){try{gtag('event',n,p||{})}catch(e){}}
document.addEventListener('submit',function(e){var f=e.target;
 if(f.matches('form.signup'))ev(f.dataset.area?'council_alert_signup':'newsletter_signup',f.dataset.area?{area:f.dataset.area}:{});
 else if(f.matches('form.fbmore'))ev('feedback_submit',{detail:'text'});},true);
document.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('button');if(!t)return;
 if(t.matches('.fbq button'))ev('feedback_submit',{answer:t.value});
 else if(t.id==='lgo')ev('levy_calculate',{area:(document.getElementById('lc')||{}).value||''});
 else if(t.id==='cp')ev('embed_code_copy',{widget:'checker'});},true);
document.addEventListener('change',function(e){var t=e.target;if(t.id==='ck-n'||t.id==='ck-c')ev('checker_use',{field:t.id==='ck-n'?'nation':'council',value:t.value});},true);
document.addEventListener('copy',function(e){var t=e.target;if(t&&t.closest&&t.closest('textarea[aria-label="Embed code"]'))ev('embed_code_copy',{widget:'levy'});},true);
})();
/* First-party signup source capture: sessionStorage only, no cookies. First touch per session. */
(function(){try{var S=sessionStorage;if(S.getItem('ukslr_src'))return;var q=new URLSearchParams(location.search),o={},k=['utm_source','utm_medium','utm_campaign'];k.forEach(function(n){var v=q.get(n);if(v)o[n]=v.slice(0,100);});var r='';try{r=document.referrer?new URL(document.referrer).hostname:'';}catch(e){}if(r&&!/(^|\.)ukshortletrules\.co\.uk$/.test(r))o.referrer=r.slice(0,100);if(Object.keys(o).length)S.setItem('ukslr_src',JSON.stringify(o));}catch(e){}})();
