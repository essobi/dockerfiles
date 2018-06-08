FROM ubuntu  
MAINTAINER Gerald Fiedler <gfiedler@sftech.de>  
  
RUN apt-get update \  
&& apt-get install -y \  
squid3 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /etc/squid3.d  
COPY squid.conf /etc/squid3.d/squid.conf  
RUN sed -i "1iinclude /etc/squid3.d/*.conf" /etc/squid/squid.conf \  
&& dpkg-reconfigure squid3 \  
&& squid -z \  
&& sleep 1  
  
VOLUME "/var/spool/squid"  
CMD ["squid3", "-N"]  

