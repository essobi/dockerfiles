FROM node:6-slim  
  
ENV GOSU_VERSION 1.10  
ENV GOSU_USER 0:0  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget git && rm -rf /var/lib/apt/lists/* \  
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
  
# Install Yeoman and generator-condensation globally and  
# clean up after ourselves.  
RUN npm install -s -g yo generator-condensation \  
&& npm cache clean  
  
# Add all helper scripts  
ADD scripts/ /scripts/  
  
# make particles directory  
RUN mkdir /particles \  
&& mkdir -p /home/condensation  
  
WORKDIR /particles  
  
VOLUME ["/home/condensation","/particles"]  
  
ENTRYPOINT ["/scripts/entry"]  

