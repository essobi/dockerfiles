FROM nginx  
  
MAINTAINER Matt Oddie <docker@mattoddie.com>  
  
COPY ./hugo_0.15_linux_amd64 /usr/local/bin/hugo  
  
ONBUILD ADD . /site  
ONBUILD RUN hugo -s /site -d /usr/share/nginx/html  

