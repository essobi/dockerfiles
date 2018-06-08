FROM binhex/arch-base:latest  
MAINTAINER binhex  
  
# add install bash script  
COPY setup /setup  
RUN chmod +x /setup/*.sh  
  
# add supervisor conf file for app  
COPY content/conf/*.conf /etc/supervisor/conf.d/  
  
# add bash script to run openvpn  
COPY content/root/*.sh /root/  
  
# add pia certificates and sample openvpn.ovpn file  
COPY content/config/pia/* /home/nobody/  
  
# install app  
#############  
# make executable and run bash scripts to install app  
RUN chmod +x /root/*.sh  
  
# setup aur access for a new user "docker"  
RUN /bin/bash /setup/add-aur.sh docker  
RUN /bin/bash /setup/install.sh  
RUN ["rm", "-rf", "/setup"]  
  
CMD ["/bin/bash", "/root/start-arch-openvpn.sh"]  

