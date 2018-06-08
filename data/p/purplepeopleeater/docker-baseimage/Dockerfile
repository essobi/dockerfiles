FROM ubuntu:wily  
MAINTAINER trophaeum <cameron.brunner@gmail.com>  
  
RUN apt-get update && apt-get install -y apt-transport-https  
ADD . /bd_build  
COPY sources.list.xenial /etc/apt/sources.list  
#COPY sources.list /etc/apt/sources.list  
#COPY acng/apt-avahi-discover.py /usr/local/bin/apt-avahi-discover.py  
#COPY proxy/squid-avahi-discover.py /usr/local/bin/squid-avahi-discover.py  
#COPY acng/00-auto-acng /etc/apt/apt.conf.d/00-auto-acng  
RUN /bd_build/prepare.sh && \  
/bd_build/system_services.sh && \  
/bd_build/utilities.sh && \  
/bd_build/cleanup.sh  
  
COPY ssh_config /etc/ssh/ssh_config  
  
CMD ["/sbin/my_init"]  

