FROM overripe/arch-openvpn  
MAINTAINER overripe  
  
# additional files  
##################  
# add install bash script  
COPY setup /setup  
RUN chmod +x /setup/*.sh && /bin/bash /setup/install.sh  
RUN ["rm", "-rf", "/setup"]  
  
# add supervisor conf file for app  
COPY content/conf/*.conf /etc/supervisor/conf.d/  
  
COPY content/root/*.sh /root/  
COPY content/nobody/*.sh /home/nobody/  
  
RUN chmod +x /home/nobody/*.sh /root/*.sh  
  
# map /config to host defined config path (used to store configuration from
app)  
VOLUME /config  
  
# run script to set uid, gid and permissions  
CMD ["/bin/bash", "/root/start-arch-sickragevpn.sh"]  

