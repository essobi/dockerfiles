FROM hammy556/perforce-base  
MAINTAINER Hammy556  
  
# Install the perforce server  
RUN apt-get install -y perforce-server curl  
  
# Volumes for server roots and triggers  
VOLUME /opt/perforce/servers  
VOLUME /opt/perforce/triggers  
  
# Add startup file and run it by default  
COPY run.sh /  
CMD ["/run.sh"]  

