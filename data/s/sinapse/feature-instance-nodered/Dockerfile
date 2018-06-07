FROM sinapse/nodered  
COPY package.json /data/  
VOLUME /data  
CMD npm set registry $NPM_REGISTRY && \  
npm install && \  
cd /usr/src/node-red/ && \  
npm install node-red-contrib-ldap-auth-userdata && \  
/usr/src/node-red/node_modules/node-red/red.js --userDir /data --settings
/settings/settings.js  

