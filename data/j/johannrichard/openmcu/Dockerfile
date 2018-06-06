# Based on "Trusty" (14.04) baseimage  
FROM phusion/baseimage:0.9.18  
ENV PREFIX="/opt"  
# Install (witha resounding "YES" :-))  
RUN add-apt-repository -y ppa:rayanayar/openmcu-ru && \  
apt-get update && \  
apt-get install -y openmcu-ru  
  
# Expose some ports  
EXPOSE 5060 5061 1420 1554 1720  
# TODO: Add volumes for data / config  
VOLUME ["/var/lib/openmcu-ru/"]  
VOLUME ["/var/log/openmcu-ru/"]  
  
# Configuration  
ADD src/openmcu-ru.default /etc/default/openmcu-ru  
  
# Run that thing  
RUN mkdir /etc/service/openmcud  
ADD src/openmcud.sh /etc/service/openmcud/run  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]

