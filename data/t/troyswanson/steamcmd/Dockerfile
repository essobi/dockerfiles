FROM debian:wheezy  
MAINTAINER troyswanson <gerphimum@gmail.com>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
lib32gcc1 \  
curl  
  
RUN \  
mkdir -p /opt/steamcmd && \  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | \  
tar -zxC /opt/steamcmd  
  
VOLUME /var/lib/steam  
  
CMD /opt/steamcmd/steamcmd.sh \  
+login anonymous \  
+force_install_dir /var/lib/steam \  
+app_update $APP_ID validate \  
+quit  

