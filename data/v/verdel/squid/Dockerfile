FROM ubuntu:14.04  
MAINTAINER Vadim "Verdel" Aleksandrov <valeksandrov@me.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get -qy update \  
&& apt-get -qy upgrade \  
&& apt-get install -qy squid3 apache2-utils  
  
# Add config file  
ADD squid.conf /etc/squid3/squid.conf  
  
# Add startup script  
ADD squid.sh /squid.sh  
RUN chmod 755 /squid.sh  
  
# Clean install  
RUN apt-get -qy autoclean \  
&& apt-get -qy autoremove \  
&& apt-get -qy clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/src/*  
  
# Expose squid port  
EXPOSE 3128  
#Run squid  
CMD ["/squid.sh"]

