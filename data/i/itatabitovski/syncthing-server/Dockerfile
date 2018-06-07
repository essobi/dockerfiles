FROM itatabitovski/debian:jessie  
  
ENV SYNCTHING_DIR /opt/syncthing  
ENV SYNCTHING_DISCOSRV_VERSION v0.14.5  
ENV SYNCTHING_RELAYSRV_VERSION v0.14.5  
RUN apt-install wget \  
ca-certificates && \  
mkdir $SYNCTHING_DIR && \  
wget
https://github.com/syncthing/discosrv/releases/download/$SYNCTHING_DISCOSRV_VERSION/stdiscosrv-
linux-amd64-$SYNCTHING_DISCOSRV_VERSION.tar.gz && \  
tar xf stdiscosrv-linux-amd64-$SYNCTHING_DISCOSRV_VERSION.tar.gz -C
$SYNCTHING_DIR \--strip-components 1 && \  
wget
https://github.com/syncthing/relaysrv/releases/download/$SYNCTHING_RELAYSRV_VERSION/strelaysrv-
linux-amd64-$SYNCTHING_RELAYSRV_VERSION.tar.gz && \  
tar xf strelaysrv-linux-amd64-$SYNCTHING_RELAYSRV_VERSION.tar.gz -C
$SYNCTHING_DIR \--strip-components 1 && \  
rm *.tar.gz && \  
apt-purge wget  

