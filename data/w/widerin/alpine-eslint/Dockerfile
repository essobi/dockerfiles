FROM mhart/alpine-node:latest  
MAINTAINER Daniel Widerin <daniel@widerin.net>  
  
ENV ESLINT_VERSION=3.0.0 \  
ESLINT_GOOGLE=0.6.0 \  
PATH=/usr/lib/node_modules/.bin:$PATH  
  
RUN npm install -g eslint@${ESLINT_VERSION} \  
eslint-config-google@${ESLINT_GOOGLE} && \  
rm -rf /usr/share/man /tmp/* \  
/root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf  
  
CMD /usr/lib/node_modules/.bin/eslint  

