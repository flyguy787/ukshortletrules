document.querySelectorAll('.fb').forEach(function(box){
  var f=box.querySelector('form'),q=box.querySelector('.fbq'),more=box.querySelector('.fbmore'),m=box.querySelector('.fbmsg'),ans='';
  box.querySelectorAll('.fbq button').forEach(function(b){b.addEventListener('click',function(){
    ans=b.value;q.hidden=true;more.hidden=false;box.querySelector('textarea').focus();});});
  f.addEventListener('submit',function(ev){
    ev.preventDefault();var s=f.querySelector('button[type=submit]');
    if(f.website.value){more.hidden=true;m.textContent='Thanks for your feedback!';return;}
    s.disabled=true;m.textContent='Sending...';
    fetch(box.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({page:location.pathname,answer:ans,text:f.text.value,email:f.email.value,website:f.website.value})})
      .then(function(r){return r.json().catch(function(){return {ok:false};});})
      .then(function(j){if(j.ok){more.hidden=true;m.textContent='Thanks for your feedback! It helps us keep the rules accurate.';m.focus();}else{m.textContent=j.error||'Sorry, something went wrong. Please try again.';}})
      .catch(function(){m.textContent='Sorry, something went wrong. Please try again.';})
      .finally(function(){s.disabled=false;});
  });
});
