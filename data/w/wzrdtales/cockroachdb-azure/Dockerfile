FROM debian:stretch  
  
MAINTAINER Tobias Gurtzick  
  
RUN apt-get update && apt-get install ntp curl python -y && apt-get clean \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ntpd.conf /etc/ntp.conf  
COPY boot.sh /  
  
WORKDIR /root/  
  
ENTRYPOINT [ "bash", "/boot.sh" ]  

