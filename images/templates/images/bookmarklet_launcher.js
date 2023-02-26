(function()
{
    if(!window.bookmarklet)
    {
        bookmarklet_js=document.body.appendChild(document.createElement('script'));
        bookmarklet_js.src='//socialsite.com:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*9999999999999999);
        window.bookmarklet=true;
    }
    else
    {
        bookmarkletLaunch();
    }
})();


// The preceding script checks whether the bookmarklet has already been loaded by checking the value 
// of the bookmarklet window variable with if(!window.bookmarklet):
// • If window.bookmarklet is not defined or doesn’t have a truthy value (considered true in a 
// Boolean context), a JavaScript file is loaded by appending a script element to the body 
// of the HTML document loaded in the browser. The src attribute is used to load the URL of 
// the bookmarklet.js script with a random 16-digit integer parameter generated with Math.
// random()*9999999999999999. Using a random number, we prevent the browser from loading 
// the file from the browser’s cache. If the bookmarklet JavaScript has been previously loaded, 
// the different parameter value will force the browser to load the script from the source URL 
// again. This way, we make sure the bookmarklet always runs the most up-to-date JavaScript code.
// • If window.bookmarklet is defined and has a truthy value, the function bookmarkletLaunch()
// is executed. We will define bookmarkletLaunch() as a global function in the bookmarklet.js