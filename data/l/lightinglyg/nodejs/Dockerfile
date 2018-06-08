FROM hub.c.163.com/lightingfire/alpine-base:3.4  
  
MAINTAINER Lighting <liuyg@liuyingguang.cn>  
  
#ENV NODE_VERSION=v4.5.0 NPM_VERSION=2  
#ENV NODE_VERSION=v5.12.0 NPM_VERSION=3  
ENV NODE_VERSION=v6.9.1 NPM_VERSION=v3.10.8  
  
RUN apk add --no-cache curl make gcc g++ python linux-headers paxctl libgcc
libstdc++ \  
&& mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& curl -sSL
http://cdn.npm.taobao.org/dist/node/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz
| tar -zx \  
&& cd node-${NODE_VERSION} \  
&& export GYP_DEFINES="linux_use_gold_flags=0" \  
&& ./configure --prefix=/usr \  
&& make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make install \  
&& paxctl -cm /usr/bin/node \  
&& cd /root \  
&& if [ -x /usr/bin/npm ]; then \  
npm install -g npm@${NPM_VERSION} && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
fi \  
&& apk del make gcc g++ python linux-headers paxctl \  
&& rm -rf /usr/local/src /tmp/* /usr/share/man /var/cache/apk/* \  
/root/.npm /root/.node-gyp /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html \  
&& mv -f /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh  
  
#COPY aliases.sh /etc/profile.d/  

