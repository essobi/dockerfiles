FROM node:4  
MAINTAINER Helder Correia <me@heldercorreia.com>  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& curl -sSLo /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -sSLo /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# create unprivileged user  
RUN groupadd -r node && useradd -m -r -g node node  
RUN chown -R node:node /usr/local  
ENV PATH node_modules/.bin:$PATH  
  
# install bower globally  
RUN gosu node npm install -g bower  
  
# silence usage statistics question in bower  
RUN mkdir -p /home/node/.config/configstore && \  
echo "{\"optOut\": true}" > /home/node/.config/configstore/insight-bower.json
&& \  
chown -R node:node /home/node  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
WORKDIR /data  

