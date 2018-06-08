FROM openjdk:8-jre  
MAINTAINER MEDEVIT <office@medevit.at>  
ARG BRANCH=master  
  
RUN apt-get update && apt-get install -y openvpn && apt-get clean && rm -rf
/var/lib/apt/lists/*  
RUN adduser --disabled-password --gecos "" \--home /elexis elexis && \  
wget http://download.elexis.info/elexis-
server/${BRANCH}/products/info.elexis.server.runtime.product-
linux.gtk.x86_64.zip && \  
unzip info.elexis.server.runtime.product-linux.gtk.x86_64.zip -d /opt/elexis-
server && \  
rm info.elexis.server.runtime.product-linux.gtk.x86_64.zip && \  
mkdir -p /elexis/elexis-server/logs && \  
chown -R elexis:elexis /opt/elexis-server /elexis  
  
COPY releng/docker-assets/elexis-server.sh /  
  
USER elexis  
WORKDIR /elexis  
  
USER elexis  
EXPOSE 8480  
EXPOSE 8380  
EXPOSE 7234  
VOLUME /elexis  
  
CMD ["/elexis-server.sh"]  

