FROM node:6.5.0  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
RUN mkdir -p /home/user && chmod 777 /home/user ; \  
mkdir -p /data/npm && chmod 777 /data/npm  
  
VOLUME /home/user  
ENV HOME="/home/user" \  
NPM_CONFIG_PREFIX="/data/npm"  
RUN npm install -g angular-cli@1.0.0-beta.11-webpack.8 process-nextick-args
util-deprecate typings gulp \  
&& npm cache clean  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

