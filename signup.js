document.querySelectorAll('form.signup').forEach(function(f){
  f.addEventListener('submit',function(ev){
    ev.preventDefault();var m=f.querySelector('.msg'),url=f.dataset.endpoint;
    if(f.website.value){return;}
    if(!url){m.textContent='Signups open very soon. Thanks for your interest!';return;}
    m.textContent='Subscribing...';
    fetch(url,{method:'POST',mode:'no-cors',body:new URLSearchParams({email:f.email.value})})
      .then(function(){m.textContent='Thanks! You\'re on the list.';f.reset();})
      .catch(function(){m.textContent='Sorry, something went wrong. Please try again.';});
  });
});
