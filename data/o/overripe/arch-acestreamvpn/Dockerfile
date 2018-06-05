FROM overripe/arch-openvpn  
MAINTAINER overripe  
  
# additional files  
##################  
COPY setup /setup  
RUN chmod +x /setup/*.sh  
  
# run install bash script  
RUN /bin/bash /setup/install.sh  
RUN ["rm", "-rf", "/setup"]  
  
# install aceproxy  
RUN git clone https://github.com/ValdikSS/aceproxy.git /home/nobody/aceproxy  
  
# add supervisor conf file for app  
COPY content/conf/*.conf /etc/supervisor/conf.d/  
  
COPY content/root/*.sh /root/  
COPY content/nobody/*.sh /home/nobody/  
  
RUN chmod +x /home/nobody/*.sh /root/*.sh  
  
# run script to set uid, gid and permissions  
CMD ["/bin/bash", "/root/start-arch-acestreamvpn.sh"]  

