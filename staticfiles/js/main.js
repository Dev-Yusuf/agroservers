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
window.addEventListener('mouseover', initLandbot, { once: true });
window.addEventListener('touchstart', initLandbot, { once: true });
    var myLandbot;
    function initLandbot() {
      if (!myLandbot) {
        var s = document.createElement('script');s.type = 'text/javascript';s.async = true;
        s.addEventListener('load', function() {
          myLandbot = new Landbot.Popup({
            configUrl: 'https://chats.landbot.io/v3/H-1247231-28FXUG69T7XDWFOH/index.json',
          });
        });
        s.src = 'https://cdn.landbot.io/landbot-3/landbot-3.0.0.js';
        var x = document.getElementsByTagName('script')[0];
        x.parentNode.insertBefore(s, x);
      }
    }
//GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

//ENSURE SEARCH FORM EXISTS
if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()

            //GET THE DATA ATTRIBUTE
            let page = this.dataset.page

            //ADD HIDDEN SEARCH INPUT TO FORM
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`


            //SUBMIT FORM
            searchForm.submit()
        })
    }
}


