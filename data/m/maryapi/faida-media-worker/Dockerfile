FROM mhart/alpine-node:8.5.0  
MAINTAINER MarYapı <membership@maryapi.com.tr>  
  
WORKDIR /app  
ADD . .  
  
RUN apk update && \  
apk add --no-cache vips-dev fftw-dev --update-cache --repository
https://dl-3.alpinelinux.org/alpine/edge/testing/ && \  
apk add --no-cache git make gcc g++ python && \  
npm install --unsafe-perm --production && \  
apk del git make gcc g++ python && \  
rm -rf /etc/ssl \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
CMD ["npm", "start"]  

