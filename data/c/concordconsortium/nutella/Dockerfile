FROM ruby:2.2  
LABEL Description="Nutella Container" Vendor="Concord Consortium"
Version="0.1"  
  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 7.6.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN gem install nutella_framework  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ precise main universe" >>
/etc/apt/sources.list  
RUN apt-get -q -y update  
RUN apt-get install -y tmux  
  
#add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
numactl \  
&& rm -rf /var/lib/apt/lists/*  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
ENV GPG_KEYS \  
# pub 4096R/A15703C6 2016-01-11 [expires: 2018-01-10]  
# Key fingerprint = 0C49 F373 0359 A145 1858 5931 BC71 1F9B A157 03C6  
# uid MongoDB 3.4 Release Signing Key <packaging@mongodb.com>  
0C49F3730359A14518585931BC711F9BA15703C6  
RUN set -ex; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --export $GPG_KEYS > /etc/apt/trusted.gpg.d/mongodb.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
ENV MONGO_MAJOR 3.4  
ENV MONGO_VERSION 3.4.2  
ENV MONGO_PACKAGE mongodb-org  
  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-
org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
${MONGO_PACKAGE}=$MONGO_VERSION \  
${MONGO_PACKAGE}-server=$MONGO_VERSION \  
${MONGO_PACKAGE}-shell=$MONGO_VERSION \  
${MONGO_PACKAGE}-mongos=$MONGO_VERSION \  
${MONGO_PACKAGE}-tools=$MONGO_VERSION \  
&& rm -rf /var/lib/mongodb \  
&& mv /etc/mongod.conf /etc/mongod.conf.orig  
  
RUN mkdir -p /data/db /data/configdb \  
&& chown -R mongodb:mongodb /data/db /data/configdb  
RUN npm install mosca pino -g  
RUN apt-get install -y vim  
RUN apt-get install -y unzip  
  
ADD nutella-config.json /root/.nutella/config.json  
ADD broker-startup /root/.nutella/broker/startup  
RUN chmod u+x /root/.nutella/broker/startup  
  
ADD startup.sh /startup.sh  
RUN chmod u+x /startup.sh  
  
RUN cd / && nutella new app  
EXPOSE 57880  
CMD ["/usr/bin/nohup","/startup.sh"]

