FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
stunnel \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
COPY stunnel.conf /etc/stunnel/  
COPY confs-available/ /etc/stunnel/confs-available/  
  
RUN \  
mkdir -vp /etc/stunnel/conf.d/ && \  
ln -vs \  
/etc/stunnel/confs-available/10-global-CA \  
/etc/stunnel/confs-available/10-global-compression-deflate \  
/etc/stunnel/confs-available/10-global-options-disable-ssl \  
/etc/stunnel/confs-available/10-global-verify-peer \  
/etc/stunnel/conf.d/  
  
ENTRYPOINT [ "stunnel" ]  

