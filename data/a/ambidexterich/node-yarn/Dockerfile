FROM ubuntu:xenial  
LABEL maintainer="github@rhamburg.com"  
  
ENV NODE_VERSION 8.10.0  
  
RUN apt-get update && apt-get install -y python g++ make curl \  
&& cd /root \  
&& curl -LSO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz" \  
&& tar -zxvf "node-v$NODE_VERSION.tar.gz" \  
&& cd node-v$NODE_VERSION \  
&& ./configure --without-npm \  
&& make -j4 \  
&& make install \  
&& cd .. && rm -rf node-v$NODE_VERSION && rm node-v$NODE_VERSION.tar.gz \  
&& apt-get purge -y python g++ make && apt-get autoremove -y  
  
ENV YARN_VERSION 1.5.1  
  
RUN set -ex \  
&& curl -LSO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn \--strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz \  
&& apt-get purge -y curl && apt-get autoremove -y  

