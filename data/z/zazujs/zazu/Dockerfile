FROM mhart/alpine-node:5  
ADD package.json /tmp/package.json  
  
RUN apk add --update --no-cache git python build-base \  
&& cd /tmp && npm install \  
&& apk del git python build-base \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /opt/app \  
&& cp -a /tmp/node_modules /opt/app/ \  
&& rm -rf /tmp/node_modules /tmp/package.json  
  
WORKDIR /opt/app  
ADD . /opt/app  
  
EXPOSE 4000  
CMD ["node", "server.js"]  

