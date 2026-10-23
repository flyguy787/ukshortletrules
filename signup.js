document.querySelectorAll('form.signup').forEach(function(f){
  f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var m=f.querySelector('.msg'),b=f.querySelector('button'),url=f.dataset.endpoint;
    if(f.website.value){m.textContent='Thanks!';return;}
    if(!url){m.textContent='Signups open very soon. Thanks for your interest!';return;}
    m.textContent='Subscribing...';b.disabled=true;
    fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.assign({email:f.email.value,website:f.website.value},f.dataset.area?{area:f.dataset.area}:{}))})
      .then(function(r){return r.json().catch(function(){return {ok:false};});})
      .then(function(j){
        if(j.ok){m.textContent=f.dataset.area?'Thanks! Alerts are on, and you\'re on the weekly "what changed" email.':'Thanks! You\'re on the list for the weekly "what changed" email.';f.reset();}
        else{m.textContent=j.error||'Sorry, something went wrong. Please try again.';}
      })
      .catch(function(){m.textContent='Sorry, something went wrong. Please try again.';})
      .finally(function(){b.disabled=false;});
  });
});
