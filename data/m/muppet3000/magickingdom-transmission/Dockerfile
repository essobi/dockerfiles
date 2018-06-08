FROM centos:7  
MAINTAINER Chris Straffon <muppet_3000@hotmail.com>  
  
RUN yum update -y && \  
yum install -y epel-release && \  
yum install -y initscripts transmission transmission-daemon && \  
yum clean all && \  
rm -rf /var/tmp/*  
  
#Add groups to allow write out to torrents directory  
RUN groupadd -g 3010 torrents_admins && \  
usermod -a -G torrents_admins transmission  
  
VOLUME ["/var/lib/transmission","/media/torrents","/media/shared"]  
  
EXPOSE 9091 51413  
USER transmission  
  
CMD /usr/bin/transmission-daemon -g /var/lib/transmission/ --foreground --log-
info  

