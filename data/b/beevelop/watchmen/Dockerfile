FROM beevelop/nodejs  
  
ENV NODE_ENV=production \  
WATCHMEN_VERSION=3.4.0 \  
WATCHMEN_WEB_PORT=3000 \  
WATCHMEN_REDIS_PORT_PRODUCTION=6379 \  
WATCHMEN_REDIS_ADDR_PRODUCTION=redis  
  
WORKDIR /opt/watchmen  
  
RUN apt-get update && apt-get install -y curl git && \  
npm i -g bower pm2 && \  
curl -sL
"https://api.github.com/repos/iloire/watchmen/tarball/${WATCHMEN_VERSION}" |
tar xz -C . --strip-components=1 && \  
npm i && bower i --allow-root  
  
RUN npm i --save https://github.com/beevelop/watchmen-plugin-console && \  
npm i --save watchmen-plugin-pushover  
  
COPY process.yml ./  
  
CMD pm2-docker process.yml  
  
EXPOSE 3000  

