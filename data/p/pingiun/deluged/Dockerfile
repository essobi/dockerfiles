FROM ubuntu:16.04  
  
MAINTAINER Jelle Besseling <jelle@pingiun.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install deluged deluge-web  
  
ENV DLDATA /downloads  
VOLUME ["/downloads"]  
  
COPY config /config  
  
COPY deluged-entrypoint.sh /  
  
EXPOSE 58846  
  
ENTRYPOINT ["/deluged-entrypoint.sh"]  
  
CMD ["deluged"]

