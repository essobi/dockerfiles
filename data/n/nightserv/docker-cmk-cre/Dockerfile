#  
FROM debian:stretch  
MAINTAINER "MrWorta <mrworta@gmail.com>"  
EXPOSE 5000 6557  
ARG CMK_PKG=https://mathias-kettner.de/support/1.4.0p30/check-mk-
raw-1.4.0p30_0.stretch_amd64.deb  
ARG CMK_SITE  
RUN /bin/bash -c 'apt-get update; apt-get install -y curl'  
RUN curl $CMK_PKG -o /tmp/cmk.deb  
  
RUN /bin/bash -c 'apt-get install -y /tmp/cmk.deb'  
WORKDIR /opt/omd  
  
COPY Entrypoint /opt/Entrypoint  
ENTRYPOINT /bin/bash /opt/Entrypoint  

