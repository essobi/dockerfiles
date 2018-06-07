FROM binhex/arch-openvpn  
  
# additional files  
##################  
# add supervisor conf file for app  
ADD build/*.conf /etc/supervisor/conf.d/  
  
# add bash scripts to install app  
ADD build/root/*.sh /root/  
  
# add bash script to setup iptables  
ADD run/root/*.sh /root/  
  
# add bash script to run deluge  
ADD run/nobody/*.sh /home/nobody/  
  
# add python script to configure deluge  
ADD run/nobody/*.py /home/nobody/  
  
# add pre-configured config files for deluge  
ADD config/nobody/deluge/ /home/nobody/  
ADD config/nobody/webui/ /home/nobody/  
  
# add pre-configured files for sonarr  
ADD config/nobody/sonarr /  
  
# add pre-configured files for radarr  
ADD config/nobody/radarr /  
  
# add pre-configured files for jackett  
ADD config/nobody/jackett /  
  
# set environment variables  
###########################  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV XDG_CONFIG_HOME="/config/xdg"  
ADD config/nobody/ /home/nobody/  
  
# install app  
#############  
# make executable and run bash scripts to install app  
RUN chmod +x /root/*.sh /home/nobody/*.sh /home/nobody/*.py && \  
/bin/bash /root/install.sh  
  
# docker settings  
#################  
# map /config to host defined config path (used to store configuration from
app)  
VOLUME /config  
  
# map /data to host defined data path (used to store data from app)  
VOLUME /data  
  
# expose port for deluge webui  
EXPOSE 8112  
# expose port for privoxy  
EXPOSE 8118  
# expose port for deluge daemon (used in conjunction with LAN_NETWORK env var)  
EXPOSE 58846  
# expose port for deluge incoming port (used only if VPN_ENABLED=no)  
EXPOSE 58946  
EXPOSE 58946/udp  
  
# expose port for sonarr webui  
EXPOSE 8989  
# expose port for radarr webui  
EXPOSE 7878  
# expose port for radarr webui  
EXPOSE 9117  
# set permissions  
#################  
# run script to set uid, gid and permissions  
CMD ["/bin/bash", "/root/init.sh"]  
HEALTHCHECK \--interval=200s --timeout=100s CMD /healthcheck.sh || exit 1  

