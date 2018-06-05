FROM node:7.4-alpine  
  
MAINTAINER Jiri Zuna <jiri@zunovi.cz>  
  
RUN npm install -g now@4.0.0 \  
&& apk update \  
&& apk add bash \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /data  
VOLUME /data  
  
CMD ["/usr/local/bin/now"]  

