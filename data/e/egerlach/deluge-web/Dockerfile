FROM debian:stretch  
  
ENV GOSU_VERSION=1.10 \  
DELUGE_USER_ID=1000 \  
DELUGE_GROUP_ID=1000  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
deluge-common \  
deluge-web \  
procps \  
jq \  
moreutils \  
ca-certificates \  
wget \  
gnupg \  
&& rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for server in $(shuf -e ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu) ; do \  
gpg --keyserver "$server" \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && break || : ; \  
done \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
COPY entrypoint.sh /  
COPY hostlist.conf.1.2 /  
COPY web.conf /  
  
VOLUME "/var/lib/deluged/web-config"  
  
EXPOSE 8112  
CMD ["/bin/bash", "/entrypoint.sh"]  
  

