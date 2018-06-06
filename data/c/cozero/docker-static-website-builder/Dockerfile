FROM node:8  
MAINTAINER John Stewart <jstewart@cozero.com.au> and JezNag
<jnagel@cozero.com.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /app  
  
ADD . /app  
  
RUN NODE_ENV=dev npm install  
  
ENTRYPOINT npm run build  

