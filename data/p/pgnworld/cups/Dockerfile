FROM pgnworld/base:latest  
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
# Cups  
ADD install.sh /tmp/install.sh  
RUN chmod +x /tmp/install.sh  
RUN /bin/bash /tmp/install.sh  
  
# Config  
ADD xinit-cups /etc/xinetd.d/cups  
  
# End conf  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /etc/cups/  
VOLUME /var/log/cups  
VOLUME /var/spool/cups  
VOLUME /var/cache/cups  
  
EXPOSE 515 631  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
CMD ["/usr/local/bin/run.sh"]

