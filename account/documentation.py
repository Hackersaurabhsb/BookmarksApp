# # we have installed pyOpenSSL to serve our website through https instead of http
# # werkzeug to work with RunServerPlus of django extension
# # RunServerPlus is a part of django extension which works with our site to run it with https


# ####################################################################################
# #----------------- python manage.py runserver_plus --cert-file cert.crt_____________#
# # We have provided a file name to the runserver_plus command for the SSL/TLS certificate. Django 
# # Extensions will generate a key and certificate automatically.
# # Open https://mysite.com:8000/account/login/ in your browser. Now you are accessing your site 
# # through HTTPS. Note we are now using https:// instead of http://.
# # Your browser will show a security warning because you are using a self-generated certificate instead 
# # of a certificate trusted by a Certification Authority (CA).
# ############################################################################################
# #CHAPTER 3
# # to download the images from the given url we have installed requests python module 
# #the requests python module create a http get request



# #what is bookmarklet?
# # A bookmarklet is a bookmark stored in a web browser that contains JavaScript code to extend the 
# # browser’s functionality. When you click on the bookmark in the bookmarks or favorites bar of your 
# # browser, the JavaScript code is executed on the website being displayed in the browser. This is very 
# # useful for building tools that interact with other websites.


# This is how your users will add the bookmarklet to their browser and use it:
# 1. The user drags a link from your site to their browser’s bookmarks bar. The link contains JavaScript code in its href attribute. This code will be stored in the bookmark.
# 2. The user navigates to any website and clicks on the bookmark in the bookmarks or favorites 
# bar. The JavaScript code of the bookmark is executed.
# Since the JavaScript code will be stored as a bookmark, we will not be able to update it after the user 
# has added it to their bookmarks bar. This is an important drawback that you can solve by implementing 
# a launcher script. Users will save the launcher script as a bookmark, and the launcher script will load 
# the actual JavaScript bookmarklet from a URL. By doing this, you will be able to update the code of the 
# bookmarklet at any time. This is the approach that we will take to build the bookmarklet. Let’s start!