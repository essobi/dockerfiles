FROM node:8-alpine  
  
MAINTAINER sue445 <sue445@sue445.net>  
  
RUN apk --update --no-cache add bash git openssh-client  
  
RUN npm install -g heroku \  
&& rm -rf /tmp/* /root/.npm \  
&& cd /usr/local/lib/node_modules/npm/ \  
&& rm -rf man doc html *.md *.bat *.yml changelogs scripts test AUTHORS
LICENSE Makefile \  
&& find /usr/local/lib/node_modules/ -name test -o -name tests -o -name .bin
-type d | xargs rm -rf  

