FROM debian:stretch  
  
# Install dependencies  
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt -y upgrade  
RUN apt -y install gnupg2  
  
# Get OwnTracks Recorder  
RUN apt-key adv --fetch-keys
http://repo.owntracks.org/repo.owntracks.org.gpg.key  
RUN echo "deb http://repo.owntracks.org/debian stretch main" >
/etc/apt/sources.list.d/owntracks.list  
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt -y upgrade  
RUN apt -y install ot-recorder  
  
# Clean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
# Volume  
VOLUME /var/spool/owntracks/recorder  
  
# Ports  
EXPOSE 8083  
# Settings  
ENV OTR_HOST "YOURHOST"  
ENV OTR_PORT "1883"  
ENV OTR_USER "YOURUSER"  
ENV OTR_PASS "YOURPASSWORD"  
ADD ot-recorder /etc/default/ot-recorder  
  
# Command  
CMD ["/usr/sbin/ot-recorder"]  
  

