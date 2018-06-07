FROM alpine:latest  
MAINTAINER Horacio Granillo <granillo.h@gmail.com>  
  
RUN apk add --no-cache bash  
RUN apk add --no-cache openssh-client  
  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 || \  
gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
gosu nobody true; \  
\  
apk del .gosu-deps  
  
ENV ERR_PYTHON_VERSION 3  
ENV ERR_PACKAGE err  
  
COPY provisioners/base.sh /provision.sh  
RUN /provision.sh && rm /provision.sh  
  
COPY provisioners/app.sh /provision.sh  
RUN /provision.sh && rm /provision.sh  
  
COPY scripts/start.sh /bin/start.sh  
ENTRYPOINT ["/bin/start.sh"]  
  
VOLUME ["/err/data/"]  

