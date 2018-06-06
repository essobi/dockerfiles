MAINTAINER Javi Moreno <javi.moreno@capside.com>  
FROM mhart/alpine-node:4  
ENV NPM_VERSION=2  
  
RUN apk add --update git && \  
npm install -g npm@${NPM_VERSION} && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf
&& \  
rm -rf /usr/share/man /tmp/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html && \  
git clone https://github.com/ciberado/docker-workshop-footballapi.git && \  
cd api && \  
npm install  
  
  
EXPOSE 8888  
  
CMD ["node", "app.js"]

