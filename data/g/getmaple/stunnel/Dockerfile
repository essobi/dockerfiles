FROM debian:jessie-slim  
  
LABEL maintainer="Maple Team"  
  
RUN apt-get update \  
&& apt-get install -y stunnel4 \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/usr/bin/stunnel4"]  

