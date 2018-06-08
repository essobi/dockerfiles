FROM phusion/baseimage:0.9.11  
MAINTAINER Coleman Nitroy <cnitroy@me.com>  
  
RUN apt-get update  
RUN apt-get install -y python git python-zeroc-ice  
  
ADD start.sh /tmp/start.sh  
RUN chmod 755 /tmp/start.sh  
VOLUME ["/data"]  
  
RUN git clone https://github.com/mumble-voip/mumo.git  
  
WORKDIR /mumo  
CMD ["/tmp/start.sh"]

