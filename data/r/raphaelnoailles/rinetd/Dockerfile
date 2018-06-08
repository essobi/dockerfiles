FROM raphaelnoailles/baseimage:latest  
MAINTAINER Raphael Noailles <docker@noailles.de>  
  
# Set correct environment variables  
ENV HOME /root  
  
# don't ask for stupid things  
env DEBIAN_FRONTEND noninteractive  
  
# update the system  
RUN apt-get -y update && apt-get -y upgrade && dpkg-divert --local \--rename
--add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
# Start conf  
# rinetd Install  
RUN apt-get install -y rinetd  
  
# End conf  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 25 465 55553 55555  
# Use baseimage-docker's init system  
ADD scripts/start_rinetd.sh /usr/local/bin/start_rinetd.sh  
RUN chmod +x /usr/local/bin/start_rinetd.sh  
CMD ["/usr/local/bin/start_rinetd.sh"]  

