FROM debian:jessie  
  
########################################################################################################################  
### COMMON  
ENV TERM=xterm  
  
RUN apt-get update \  
&& apt-get --no-install-recommends --no-install-suggests -y install \  
ca-certificates apt-utils net-tools wget curl mc nano git \  
&& rm -rf /var/lib/apt/lists/*  
### END COMMON  
########################################################################################################################  

