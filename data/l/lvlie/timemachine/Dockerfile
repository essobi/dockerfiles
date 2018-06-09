# use ubuntu because avahi seems to work in docker, but use LTS  
FROM ubuntu:xenial  
  
MAINTAINER Leon (lvlie) Vliegenthart  
  
# update package list  
RUN apt-get update  
  
# install packages  
RUN apt-get install -y netatalk avahi-daemon && apt-get clean  
  
# add user for backup  
RUN useradd -u 800 tm  
# password will be backup, why not in my lan... :)  
RUN echo "tm:backup"|chpasswd  
  
# Add to netatalk conf  
RUN echo "- -tcp -noddp -uamlist uams_dhx.so,uams_dhx2_passwd.so
-nosavepassword" >> /etc/netatalk/afpd.conf  
  
# Create the config for the timemachine location  
RUN echo "/backup \"TM Backup\" allow:tm cnidscheme:dbd volsizelimit:500000
options:usedots,upriv,tm" >> /etc/netatalk/AppleVolumes.default  
  
# add the startup script  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# CMD can be easily overwritten for debugging  
CMD ["/start.sh"]  

