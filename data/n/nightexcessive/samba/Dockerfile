FROM phusion/baseimage:latest  
MAINTAINER Michael Johnson <michael@johnson.computer>  
RUN apt-get update \  
&& apt-get install -y samba samba-common && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY smb.conf /etc/samba/smb.conf  
COPY create-users.sh /etc/samba/create-users.sh  
COPY fix-config.sh /root/fix-config.sh  
COPY start.sh /root/start.sh  
  
CMD /root/fix-config.sh && /etc/samba/create-users.sh && exec /root/start.sh  
  
VOLUME /data/homes /data/media /etc/samba/users.conf  
EXPOSE 139 445  
EXPOSE 137/udp 138/udp  

