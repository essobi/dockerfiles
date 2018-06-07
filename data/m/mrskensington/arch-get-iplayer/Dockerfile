FROM binhex/arch-base:20170427-01  
MAINTAINER binhex  
  
# additional files  
##################  
# add supervisor conf file for app  
ADD setup/*.conf /etc/supervisor/conf.d/  
  
# add install bash script  
ADD setup/root/*.sh /root/  
  
# add start bash script  
ADD setup/nobody/*.sh /home/nobody/  
  
# install app  
#############  
# make executable and run bash scripts to install app  
RUN chmod +x /root/*.sh /home/nobody/*.sh && \  
/bin/bash /root/install.sh  
  
# docker settings  
#################  
# map /config to host defined config path (used to store configuration from
app)  
VOLUME /config  
  
# map /data to host defined data path (used to store data from app)  
VOLUME /data  
  
# set permissions  
#################  
# run script to set uid, gid and permissions  
CMD ["/bin/bash", "/root/init.sh"]

