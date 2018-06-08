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
# Install  
ADD scripts/install.sh /tmp/install.sh  
RUN chmod +x /tmp/install.sh  
RUN /bin/bash /tmp/install.sh  
  
# End conf  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /opt  
  
EXPOSE 8083 8084 8085 7072  
# Use baseimage-docker's init system  
ADD scripts/start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
CMD ["/usr/local/bin/start.sh"]  

