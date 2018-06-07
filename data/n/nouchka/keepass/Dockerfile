FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-keepass"  
LABEL version="latest"  
ENV KEEPASS_VERSION 1.8.4.1  
ENV KEEPASS_SHA256
430948219b0bc282fbf0760da7b66f72b13eee4db57de457e563342d253bd8ae  
  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/user && \  
echo "user:x:${uid}:${gid}:User,,,:/home/user:/bin/bash" >> /etc/passwd && \  
echo "user:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/user  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install keepass2 unzip wget
libmono-system-xml-linq4.0-cil libmono-system-data-datasetextensions4.0-cil
libmono-system-runtime-serialization4.0-cil mono-mcs && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget https://github.com/pfn/keepasshttp/archive/$KEEPASS_VERSION.zip && \  
unzip $KEEPASS_VERSION.zip && \  
echo "$KEEPASS_SHA256 keepasshttp-$KEEPASS_VERSION/KeePassHttp.plgx" >
SHA256SUM && \  
sha256sum -c SHA256SUM && \  
mv keepasshttp-$KEEPASS_VERSION/KeePassHttp.plgx /usr/lib/keepass2/ && \  
chmod 644 /usr/lib/keepass2/KeePassHttp.plgx  
  
USER user  
ENV HOME /home/user  
CMD /usr/bin/keepass2  

