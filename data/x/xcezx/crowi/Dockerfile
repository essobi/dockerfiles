FROM node:6.11-alpine  
  
ENV CROWI_VERSION 1.6.2  
ENV CROWI_DOWNLOAD_URL https://github.com/crowi/crowi/archive/v1.6.2.tar.gz  
ENV CROWI_DOWNLOAD_SHA 7aaaa4e95008c04658e13a103c86bea41a90433d  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
g++ \  
gcc \  
make \  
python \  
tar \  
&& curl -LO "$CROWI_DOWNLOAD_URL" \  
&& echo "$CROWI_DOWNLOAD_SHA *v$CROWI_VERSION.tar.gz" | sha1sum -c - \  
&& mkdir /crowi \  
&& tar -xzf v$CROWI_VERSION.tar.gz -C /crowi --strip-components 1 \  
&& cd /crowi \  
&& npm install --production \  
&& npm run build \  
&& apk del .build-deps  
  
WORKDIR /crowi  
  
EXPOSE 3000  
CMD ["npm", "run" "start"]  

