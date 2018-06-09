FROM openjdk:8-jdk  
  
RUN apt-get update && \  
apt-get upgrade -yq && \  
apt-get install postgresql-client -yq&& \  
apt-get autoremove -y && apt-get clean && rm -rf /var/cache/* && rm -rf
/var/tmp/* && rm -rf /tmp/*  
  
# Variables that are meant to be updated between enviorments  
# These are defaults that should ne overriden when running the image  
ENV TIGASE_DOMAIN=silf.if.pw.edu.pl \  
PGHOST=example.com \  
PGPORT=5432 \  
PGDATABASE=efizyka \  
PGUSER=tigase \  
PGPASSWORD=foo \  
TIGASE_SERVER_SOURCE=https://ocs-
pl.oktawave.com/v1/AUTH_385fff76-290b-43da-b2fc-96b1c08bce24/tools/tigase-
server-5.2.0-beta1-b3182.tar.xz \  
ADMIN_PASSWORD=changemeplease  
  
RUN adduser --disabled-password --gecos "" tigase  
  
RUN mkdir /tigase && \  
cd /tigase && \  
curl ${TIGASE_SERVER_SOURCE} > tigase.tar.xz && \  
sha256sum tigase.tar.xz | grep --quiet
6aba10301bc62cb393bbdacc575bcea2dfaaab286eada8075e8577785eccd65d && \  
tar --strip-components=1 -xaf tigase.tar.xz && \  
rm tigase.tar.xz  
  
WORKDIR /tigase  
  
COPY ./overrides/ /tigase/  
COPY ./scripts/* /tigase/scripts/  
  
CMD scripts/docker-entrypoint.sh  
  
# Websockets  
EXPOSE 5290 5291  
# Client server XMPP connection  
EXPOSE 5222  
# Server to server XMPP connection  
EXPOSE 5269  

