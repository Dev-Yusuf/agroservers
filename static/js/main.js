// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWrapper = document.querySelctor('.alert')
let alertClose = document.querySelector('.alert__close')

if(alertWrapper){
alertClose.addEventListener('click', () =>
   alertWrapper.style.display = 'none'
)
}


//THE CODE FOR THE CHATBOT 



