# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Frank Wagener <docker@dapor.de>  
  
  
# Update the repository sources list  
RUN apt-get update -q  
RUN apt-get upgrade -qy  
RUN apt-get install lsof sysstat wget openssh-server supervisor -qy  
RUN echo "wget -q -O kerio-connect-linux-64bit.deb
http://download.kerio.com/dwn/kerio-connect-linux-64bit.deb" > dl.sh  
RUN chmod +x dl.sh  
RUN ./dl.sh  
################## BEGIN INSTALLATION #########################  
RUN dpkg -i kerio-connect-linux-64bit.deb  
RUN echo "/etc/init.d/kerio-connect stop" >> /kerio-restore.sh  
RUN echo "/opt/kerio/mailserver/kmsrecover /backup/" >> /kerio-restore.sh  
RUN mkdir -p /var/log/supervisord  
RUN mkdir -p /var/run/sshd  
RUN locale-gen en_US.utf8  
RUN useradd docker -d /home/docker -g users -G sudo -m  
RUN echo docker:test123 | chpasswd  
ADD /etc/supervisor/conf.d/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
ADD /etc/init.d/kerio-connect /etc/init.d/kerio-connect  
RUN chmod +x /etc/init.d/kerio-connect  
RUN chmod +x /kerio-restore.sh  
##################### INSTALLATION END #####################  
# Expose the default portonly 4040 is nessecary for admin access  
  
EXPOSE 4040 22 25 465 587 110 995 143 993 119 563 389 636 80 443 5222 5223  
  
VOLUME /backup  
VOLUME /mailserver/data  
# Set default container command  
ENTRYPOINT ["/usr/bin/supervisord"]  
CMD ["-c", "/etc/supervisor/conf.d/supervisord.conf"]  

