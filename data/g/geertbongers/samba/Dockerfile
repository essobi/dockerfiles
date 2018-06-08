FROM geertbongers/webmin  
MAINTAINER Geert  
  
RUN apt-get update &&\  
apt-get install -y samba  
  
RUN cd /webmin-install &&\  
wget http://download.webmin.com/download/modules/samba.wbm.gz &&\  
perl ./install-module.pl ./samba.wbm.gz "${config_dir}" &&\  
wget http://download.webmin.com/download/modules/useradmin.wbm.gz &&\  
perl ./install-module.pl ./useradmin.wbm.gz "${config_dir}" &&\  
/create_default_config_webmin.sh &&\  
/create_default_config_user.sh &&\  
mkdir -p /default-config/samba-data &&\  
cp -rp /etc/samba/* /default-config/samba-data  
  
ADD start_samba.sh /etc/service/samba/run  
ADD start_netbios.sh /etc/service/netbios/run  
ADD 03_samba_setup.sh /etc/my_init.d/03_samba_setup.sh  
  
# You have to run it with --net="host" this is just for showing which port's
are gonne be used  
EXPOSE 10000  
EXPOSE 135 136 137 138 139 445  
EXPOSE 135/udp 136/udp 137/udp 138/udp 139/udp 445/udp  
  
VOLUME /samba-data  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

