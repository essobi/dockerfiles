FROM ubuntu:14.04  
MAINTAINER iTech <itech \at\ riseup.net>  
  
RUN apt-get update \  
&& apt-get install -y supervisor unattended-upgrades \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY install /install  
RUN chmod 755 install  
RUN /install  
  
COPY start /start  
RUN chmod 755 /start  
  
ENTRYPOINT ["/start"]  

