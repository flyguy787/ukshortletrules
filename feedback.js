/* Page feedback: "Was this page helpful?" vote + optional comment/email, and "Spot something wrong?" report form.
   Posts to the signup backend (/feedback), which emails hello@. localStorage only remembers that this page was voted on. */
(function(){
var z=document.querySelector('.fbz');if(!z)return;
var EP=z.getAttribute('data-endpoint'),path=location.pathname.replace(/\.html$/,'')||'/',KEY='ukslr_fb:'+path;
function ga(n,p){try{if(typeof gtag==='function')gtag('event',n,p)}catch(e){}}
function store(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
function post(d){return fetch(EP,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)}).then(function(r){return r.json().catch(function(){return{ok:false}})})}
var ERR='Sorry, that did not send. Please try again.';
/* ---- vote ---- */
var fb=z.querySelector('.fb');
if(fb){
  if(store(KEY)){fb.remove();fb=null}
}
if(fb){
  var q=fb.querySelector('.fbq'),f=fb.querySelector('.fbmore'),thx=fb.querySelector('.fbthx'),lab=f.querySelector('label[for=fbt]'),m=f.querySelector('.fbmsg'),vote='',pending=false;
  function done(){pending=false;q.hidden=true;f.hidden=true;thx.hidden=false;thx.focus()}
  function send(withText){
    var d={kind:'vote',page:path,vote:vote,website:f.website.value};
    if(withText){d.comment=f.comment.value;d.email=f.email.value}
    var b=f.querySelectorAll('button');b.forEach(function(x){x.disabled=true});m.textContent='Sending...';
    post(d).then(function(j){if(j.ok){m.textContent='';done()}else{m.textContent=j.error||ERR}})
      .catch(function(){m.textContent=ERR}).then(function(){b.forEach(function(x){x.disabled=false})});
  }
  fb.querySelectorAll('.fbv').forEach(function(b){b.addEventListener('click',function(){
    vote=b.getAttribute('data-v');pending=true;store(KEY,vote);
    fb.querySelectorAll('.fbv').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    lab.firstChild.nodeValue=vote==='up'?'Anything we should add? ':'What could be better? ';
    q.classList.add('fbdone');f.hidden=false;fb.classList.add('fbopen');f.comment.focus({preventScroll:false});
    ga('feedback_vote',{vote:vote,page_path:path});
  })});
  f.addEventListener('submit',function(ev){ev.preventDefault();if(f.website.value){done();return}send(true)});
  f.querySelector('.fbskip').addEventListener('click',function(){send(false)});
  // Vote given but neither Send nor Skip pressed before leaving: still count the vote (one email per vote).
  addEventListener('pagehide',function(){if(!pending||!navigator.sendBeacon)return;pending=false;
    navigator.sendBeacon(EP,JSON.stringify({kind:'vote',page:path,vote:vote,comment:f.comment.value,email:f.email.value,website:f.website.value}))});
}
/* ---- error report ---- */
var rp=z.querySelector('.rep');
if(rp){
  var t=rp.querySelector('.replink'),rf=rp.querySelector('form'),rm=rf.querySelector('.fbmsg'),rthx=rp.querySelector('.repthx');
  rf.querySelector('[name=pageurl]').value=location.origin+path;
  t.addEventListener('click',function(){var o=rf.hidden;rf.hidden=!o;t.setAttribute('aria-expanded',o?'true':'false');if(o)rf.comment.focus()});
  rf.querySelector('.repcancel').addEventListener('click',function(){rf.hidden=true;t.setAttribute('aria-expanded','false');t.focus()});
  rf.addEventListener('submit',function(ev){ev.preventDefault();
    if(rf.website.value){rf.hidden=true;t.hidden=true;rthx.hidden=false;return}
    if(rf.comment.value.trim().length<3){rm.textContent="Please tell us what's wrong.";rf.comment.focus();return}
    var s=rf.querySelector('button[type=submit]');s.disabled=true;rm.textContent='Sending...';
    post({kind:'report',page:path,council:rf.council?rf.council.value:'',comment:rf.comment.value,source:rf.source.value.trim(),email:rf.email.value,website:rf.website.value})
      .then(function(j){if(j.ok){rm.textContent='';rf.hidden=true;t.hidden=true;rthx.hidden=false;rthx.focus();ga('report_error',{page_path:path,council:rf.council?rf.council.value:''})}else rm.textContent=j.error||ERR})
      .catch(function(){rm.textContent=ERR}).then(function(){s.disabled=false});
  });
}
if(!fb&&!rp)z.hidden=true;
})();
