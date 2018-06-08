FROM debian:jessie  
MAINTAINER Ray Zane <rzane@bodnargroup.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -qy install \  
sqitch \  
libdbd-firebird-perl \  
firebird2.5-superclassic \  
&& apt-get clean -q  
  
RUN sed 's/ENABLE_FIREBIRD_SERVER=no/ENABLE_FIREBIRD_SERVER=yes/g'
/etc/default/firebird2.5 -i  
  
RUN service firebird2.5-superclassic start  
  
VOLUME /databases  
  
EXPOSE 3050/tcp  
  
ENTRYPOINT ["/bin/bash", "-c"]  

