# Blog dev Dockerfile  
FROM alpine:3.2  
MAINTAINER vSense <docker@vsense.fr>  
  
RUN apk -U add \  
nodejs \  
git \  
python \  
&& apk -U add --virtual build \  
alpine-sdk \  
python \  
&& npm install -g grunt-cli \  
&& git clone https://github.com/hakimel/reveal.js.git /revealjs \  
&& cd /revealjs \  
&& npm install \  
&& apk del build \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /revealjs  
  
EXPOSE 8001  
CMD ["grunt", "serve", "--port", "8001"]  

