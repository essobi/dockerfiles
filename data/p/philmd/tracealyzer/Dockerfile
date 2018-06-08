FROM debian:stable  
  
MAINTAINER f4bug@amsat.org  
  
RUN apt update && \  
DEBIAN_FRONTEND=noninteractive apt install -yy \  
curl \  
libcroco3 \  
libgail18 \  
libgtk2.0-bin \  
librsvg2-2 \  
libmono-system-windows-forms4.0-cil \  
mono-runtime && \  
apt-get clean  
  
ENTRYPOINT ["sh", "/opt/tz-helper.sh"]  
  
ADD https://raw.githubusercontent.com/philmd/docker-
tracealyzer/master/common/tz-helper.sh /opt/tz-helper.sh  
  
ENV TRACEALIZER_VERSION 3.2.0  
RUN curl -s
https://percepio.com/downloads/TzForFreeRTOS-${TRACEALIZER_VERSION}.tgz | tar
-C /opt -xzf -  

