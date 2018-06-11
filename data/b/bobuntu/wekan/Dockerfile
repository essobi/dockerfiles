FROM alpine  
  
ENV NODE_VERSION=0.10.48 WEKAN_VERSION=0.18  
  
RUN set -x && \  
apk add --no-cache bash ca-certificates libgcc libstdc++ && \  
apk add --no-cache --virtual .tools make g++ python wget libressl tar && \  
mkdir /opt && cd /opt && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget -q https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk && \  
wget -q https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-bin-2.25-r0.apk && \  
wget -q https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-i18n-2.25-r0.apk && \  
apk add glibc-2.25-r0.apk glibc-bin-2.25-r0.apk glibc-i18n-2.25-r0.apk && \  
/usr/glibc-compat/bin/localedef -i ja_JP -f UTF-8 ja_JP.UTF-8 && \  
\  
wget -q
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
&& \  
tar zxf node-v${NODE_VERSION}-linux-x64.tar.gz && \  
mv node-v${NODE_VERSION}-linux-x64 node && \  
ln -s /opt/node/bin/node /usr/local/bin/node && \  
ln -s /opt/node/bin/npm /usr/local/bin/npm && \  
npm install -g npm@latest && \  
npm config set unsafe-perm true && \  
\  
wget -q
https://github.com/wekan/wekan/releases/download/v${WEKAN_VERSION}/wekan-${WEKAN_VERSION}.tar.gz
&& \  
tar zxf wekan-${WEKAN_VERSION}.tar.gz && \  
mv bundle wekan && \  
cd wekan/programs/server && \  
npm install exit 0 && \  
npm install --save bcryptjs && npm uninstall --save bcrypt && \  
\  
apk del .tools && \  
rm -rf /opt/glibc* /opt/node-v${NODE_VERSION}-linux-x64.tar.gz
/opt/wekan-${WEKAN_VERSION}.tar.gz \  
/tmp/* /root/.npm /root/.node-gyp  
  
CMD ["node", "/opt/wekan/main.js"]  

