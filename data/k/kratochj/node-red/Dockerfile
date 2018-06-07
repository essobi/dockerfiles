FROM node:7-alpine  
  
RUN buildDeps='git alpine-sdk openssl-dev libwebsockets-dev c-ares-dev util-
linux-dev hiredis-dev curl-dev libxslt docbook-xsl'; \  
apk update && \  
apk add $buildDeps python && \  
apk del $buildDeps && rm -rf /var/cache/apk/*  
  
# Home directory for Node-RED application source code.  
RUN mkdir -p /usr/src/node-red  
  
# User data directory, contains flows, config and nodes.  
RUN mkdir /data  
  
WORKDIR /usr/src/node-red  
  
# Add node-red user so we aren't running as root.  
RUN adduser -D -h /usr/src/node-red -H node-red \  
&& chown -R node-red:node-red /data \  
&& chown -R node-red:node-red /usr/src/node-red  
  
RUN npm install -g node-red-admin  
COPY hash /bin/hash  
RUN chmod 755 /bin/hash  
  
USER node-red  
  
# package.json contains Node-RED NPM module and node dependencies  
COPY package.json /usr/src/node-red/  
RUN npm install && npm install node-red-dashboard  
  
# User configuration directory volume  
EXPOSE 1880  
VOLUME /data  
  
# Environment variable holding file path for flows configuration  
ENV FLOWS=flows.json  
  
COPY entrypoint.sh entrypoint.sh  
COPY settings.sample.js settings.sample.js  
  
CMD ["./entrypoint.sh"]

