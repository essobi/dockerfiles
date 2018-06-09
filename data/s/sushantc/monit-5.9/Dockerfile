FROM centos  
MAINTAINER Sushant Chawla  
  
RUN rpm -ivh http://intra.jadoos.com/monit-5.9-1.x86_64.rpm  
ADD monit.conf /etc/monitrc  
ADD inittab /etc/  
RUN chown root.root /etc/monitrc  
RUN chmod 700 /etc/monitrc  
EXPOSE 2812  
#CMD ["/usr/bin/monit", "-I"]  
#CMD [/usr/bin/monit -d 10 -Ic /etc/monit.conf]  
ENTRYPOINT /usr/bin/monit -I  

