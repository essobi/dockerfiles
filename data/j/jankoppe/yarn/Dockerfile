FROM alpine:3.4  
MAINTAINER Jan Koppe <post@jankoppe.de>  
ENV NODE_VER=v7.6.0  
ENV YARN_VER=v0.21.3  
RUN apk add --no-cache curl make gcc g++ python linux-headers paxctl libgcc
libstdc++ \  
&& curl -o node-${NODE_VER}.tar.gz -sSL
https://nodejs.org/dist/${NODE_VER}/node-${NODE_VER}.tar.gz \  
&& tar -zxf node-${NODE_VER}.tar.gz \  
&& cd node-${NODE_VER} \  
&& export GYP_DEFINES="linux_use_gold_flags=0" \  
&& ./configure --prefix=/usr --fully-static --without-npm \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make -j${NPROC} -C out mksnapshot BUILDTYPE=Release \  
&& paxctl -cm out/Release/mksnapshot \  
&& make -j${NPROC} \  
&& make install \  
&& paxctl -cm /usr/bin/node \  
&& rm -rf /usr/lib/node_modules/* \  
&& mkdir -p /usr/lib/node_modules/ \  
&& cd /usr/lib/node_modules \  
&& curl -o yarn-${YARN_VER}.tar.gz -sSL \  
https://github.com/yarnpkg/yarn/releases/download/${YARN_VER}/yarn-${YARN_VER}.tar.gz
\  
&& tar -zxf yarn-${YARN_VER}.tar.gz \  
&& rm yarn-${YARN_VER}.tar.gz \  
&& mv dist yarn \  
&& ln -s /usr/lib/node_modules/yarn/bin/yarn.js /usr/local/bin/yarn \  
&& apk del curl make gcc g++ python linux-headers paxctl libgcc libstdc++ \  
&& rm -rf /etc/ssl /node-${NODE_VER}.tar.gz /node-${NODE_VER} /usr/include \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
&& cd /  
  
CMD yarn  

