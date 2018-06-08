# This is a comment  
FROM openhab/openhab:2.1.0-snapshot-amd64  
MAINTAINER Mathias Henrich <mathias@henrich.eu>  
USER root  
RUN apt-get update && apt-get install -y samba-common-bin \  
libpcap-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN setcap cap_net_bind_service=+ep /usr/lib/java-8/bin/java  
USER openhab

