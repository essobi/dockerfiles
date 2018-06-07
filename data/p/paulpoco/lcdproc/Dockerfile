# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM binhex/arch-base  
  
# additional files  
##################  
# add supervisor conf file for app  
ADD setup/*.conf /etc/supervisor/conf.d/  
  
# add bash scripts to install app  
ADD setup/root/*.sh /root/  
  
# add bash script to run lcdproc  
ADD apps/nobody/*.sh /home/nobody/  
  
# add pre-configured config files for nobody  
ADD config/nobody/ /home/nobody/  
  
# install app  
#############  
# make executable and run bash scripts to install app  
RUN chmod +x /root/*.sh /home/nobody/*.sh && \  
/bin/bash /root/install.sh  
  
ADD bashrc /home/nobody/.bashrc  
  
# map /config to host defined config path (used to store configuration from
app)  
VOLUME /config  
  
# set permissions  
#################  
# run script to set uid, gid and permissions  
CMD ["/bin/bash", "/root/init.sh"]  

