FROM debian:jessie  
MAINTAINER John Paul Alcala, jp@jpalcala.com  
  
# Taken from the official Postgres Dockerfile  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
ENV DROPBOX_HOME=/opt/dropbox  
  
RUN groupadd -g 1000 dropbox && \  
useradd -g dropbox -u 1000 -r -M dropbox && \  
mkdir -p $DROPBOX_HOME && \  
wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - -C
$DROPBOX_HOME && \  
chown -R dropbox:dropbox $DROPBOX_HOME  
  
COPY dropbox /usr/local/bin/  
  
ENTRYPOINT ["dropbox"]  
CMD ["run"]  

