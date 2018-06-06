FROM mhart/alpine-node:6.3.1  
MAINTAINER Dave Finster <davefinster@me.com>  
  
WORKDIR /usr/src/app  
  
COPY ./ ./  
  
RUN set -x \  
&& apk add --no-cache --virtual .npm-deps python make gcc linux-headers
alpine-sdk \  
&& npm install \  
&& ./node_modules/.bin/grunt \  
&& rm -rf node_modules \  
&& npm install --production \  
&& apk del .npm-deps  
  
EXPOSE 8080  
CMD ["node", "app.js"]

