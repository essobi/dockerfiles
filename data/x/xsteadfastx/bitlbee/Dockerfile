FROM ubuntu:bionic  
MAINTAINER Marvin Steadfast <marvin@xsteadfastx.org>  
  
ENV TINI_VERSION v0.18.0  
  
COPY root /  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y \  
bitlbee-libpurple \  
bitlbee-plugin-facebook \  
bitlbee-plugin-otr \  
curl \  
gosu \  
gpg \  
purple-matrix \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -L
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini -o
/tini \  
&& curl -L
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc -o
/tini.asc \  
&& chmod +x /tini \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& \  
for server in $(shuf -e ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu) ; do \  
gpg --keyserver "$server" \--recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 && break || : ; \  
done \  
&& gpg --verify /tini.asc \  
&& mkdir -p /var/run/bitlbee  
  
VOLUME /data  
  
EXPOSE 6667  
  
ENTRYPOINT ["/tini", "--", "/entrypoint.sh"]  
CMD ["bitlbee"]  

