FROM node:7-alpine  
  
ENV VERSION 1.1.0  
RUN vVERSION=$(echo $VERSION | sed -E s/^[0-9]\\.+\\[0-9]+\\.[0-9]+/v\\\0/g)
&& \  
apk add --no-cache curl && \  
echo https://github.com/cheminfo/stock-printer-proxy/archive/$vVERSION.tar.gz
&& \  
curl -fSL https://github.com/cheminfo/stock-printer-
proxy/archive/$vVERSION.tar.gz -o $VERSION.tar.gz && \  
tar -xzf $VERSION.tar.gz && \  
mv stock-printer-proxy-${VERSION} stock-printer-proxy-source && \  
npm i -g pm2 && \  
cd /stock-printer-proxy-source && \  
npm i && \  
rm -rf /root/.npm /usr/local/share/.cache /root/.cache /${VERSION}.tar.gz  
  
COPY pm2-proxy.yml /pm2-proxy.yml  
  
WORKDIR /stock-printer-proxy-source  
CMD ["npm", "start"]  

