const siteurl='//127.0.0.1:8000/';
const styleurl=siteurl+'static/css/bookmarklet.css';
const minwidth=250;
const minheight=250;
console.log("load css lines executed");
// siteUrl and staticUrl: The base URL for the website and the base URL for static files.
// • minWidth and minHeight: The minimum width and height in pixels for the images that the 
// bookmarklet will collect from the site. The bookmarklet will identify images that have at least 
// 250px width and 250px height.



//load css
var head=document.getElementsByTagName('head')[0];
var link=document.createElement('link');
link.rel='stylesheet';
link.type='text/css';
link.href=styleurl+'?r='+Math.floor(Math.random()*9999999999999999);
head.appendChild(link);
// The previous code generates an object equivalent to the following JavaScript code and appends it to 
// the <head> element of the HTML page:
// <link rel="stylesheet" type="text/css" href= "//127.0.0.1:8000/static/css/
// bookmarklet.css?r=1234567890123456">



//load html

// Now we will create the HTML element to display a container on the website where the bookmarklet is 
// executed. The HTML container will be used to display all images found on the site and let users choose 
// the image they want to share. It will use the CSS styles defined in the bookmarklet.css stylesheet.

var body=document.getElementsByTagName('body')[0];
boxHtml='<div id="bookmarklet"><a href="#" id="close">&times</a> <h1>Select an image to bookmark:</h1> <div class="images"></div> </div>';
body.innerHTML+=boxHtml;
//function to show the bookmarklet container
function bookmarkletLaunch()
{
    bookmarklet=document.getElementById('bookmarklet');
    var images_found=bookmarklet.querySelector('.images');
    //clear images found
    images_found.innerHTML='';
    //display bookmarklet
    bookmarklet.style.display='block';

    //close event
    bookmarklet.querySelector('#close').addEventListener('click',function()
    {
        bookmarklet.style.display='none';
    });
    //find images with the minimun width and height
    images=document.querySelectorAll('img[src$=".jpeg"],img[src$=".jpg"],img[src$=".png"]');
    images.forEach(image=>
        {
            if(image.naturalHeight>minheight && image.naturalWidth>minwidth)
            {
                var imagefound=document.createElement('img');
                imagefound.src=image.src;
                images_found.append(imagefound);
            }
        })

        //below function is when user click on an image we direct the user to the book page by window.open() function
        images_found.querySelectorAll('img').forEach(image=>
            {
                image.addEventListener('click',function(event)//adding event listener on each image
                {
                    image_selected=event.target;//event.target get the image which is clicked by user
                    bookmarklet.style.display='none';
                    window.open(siteurl+'images/create/?url='+encodeURIComponent(image_selected.src)+'&title='+encodeURIComponent(document.title),'_blank')
                })
            })
}
console.log("this function called");
//launch the bookmarklet code
bookmarkletLaunch();