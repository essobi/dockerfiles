FROM mainlxc/ubuntu  
MAINTAINER Asokani "https://github.com/asokani"  
# TODO RUN apt-get update  
# enable ssh  
RUN rm -f /etc/service/sshd/down  
  
ADD useraccess.js /etc/my_init.d/10-useraccess.js  
  
EXPOSE 22  
CMD ["/sbin/my_init"]  
  
# TODO RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

