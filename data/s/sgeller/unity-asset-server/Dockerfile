FROM quintenk/supervisor  
  
MAINTAINER Sebastian Geller <info@cmb-tradecenter.org>  
  
ADD unity_asset_server.sv.conf /etc/supervisor/conf.d/  
ADD uas_backup.cron /etc/cron.d/  
ADD start.sh /root/start.sh  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y wget libc6:i386 zlib1g:i386 && \  
wget http://unity3d.com/files/asset-server/unity-asset-server_2.0.1_i386.deb
&& \  
dpkg -i --force-architecture unity-asset-server_2.0.1_i386.deb && \  
rm -f unity-asset-server_2.0.1_i386.deb && \  
chmod +x /root/start.sh && \  
mkdir /var/log/unity_asset_server  
  
EXPOSE 10733  
ENTRYPOINT ["/root/start.sh"]

