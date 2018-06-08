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
# SAP Service  
RUN mkdir -p /usr/sap  
RUN touch /usr/sap/sap.log  
ADD scripts/saprouttab /usr/sap/saprouttab  
  
ADD scripts/start.services.txt /tmp/start.services.txt  
ADD scripts/sapd.services.txt /tmp/sapd.services.txt  
ADD scripts/sapg.services.txt /tmp/sapg.services.txt  
RUN cat /tmp/start.services.txt >> /etc/services  
RUN cat /tmp/sapd.services.txt >> /etc/services  
RUN cat /tmp/sapg.services.txt >> /etc/services  
  
# End conf  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /usr/sap  
  
EXPOSE 3299  
# Use baseimage-docker's init system  
ADD scripts/startsap.sh /usr/local/bin/startsap.sh  
RUN chmod +x /usr/local/bin/startsap.sh  
CMD ["/usr/local/bin/startsap.sh"]  

