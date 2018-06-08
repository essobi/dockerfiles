FROM docker  
MAINTAINER Pedro Melo <melo@simplicidade.org>  
  
RUN apk add --no-cache git nodejs nodejs-npm \  
&& npm install -g uglifyjs csso \  
&& rm -rf /var/cache/apk/*  

