FROM alpine:3.7  
MAINTAINER stormis  
  
RUN apk add --update nodejs && \  
npm install -g npm@3.10.3 && \  
rm -rf /usr/share/man /tmp/* /var/tmp/* /var/cache/apk/* /root/.npm
/root/.node-gyp /usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
COPY package.json /app/package.json  
WORKDIR /app/  
  
RUN apk add --update git python build-base curl bash && \  
echo "Fixing PhantomJS" && \  
curl -Ls
"https://github.com/dustinblackman/phantomized/releases/download/2.1.1/dockerized-
phantomjs.tar.gz" | tar xz -C / && \  
echo "Installing node modules" && \  
sed -i '/postinstall/d' package.json && \  
npm install --production && \  
apk del git python build-base curl && \  
rm -rf /usr/share/man /tmp/* /var/tmp/* /var/cache/apk/* /root/.npm
/root/.node-gyp  
  
COPY . /app/  
  
ENV PORT 3000  
EXPOSE $PORT  
  
CMD ["npm", "run", "start"]

