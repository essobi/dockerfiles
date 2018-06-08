FROM debian:stretch-slim  
  
LABEL description="Script for clean useless file in rtorrent" \  
tags="latest" \  
maintainer="magicalex <magicalex@mondedie.fr>"  
  
ENV RPC_PORT=8080  
RUN apt-get update && apt-get install -y -q --no-install-recommends libxmlrpc-
core-c3-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/cache/debconf/*-old  
  
COPY rtCleaner.sh /usr/local/bin/rtcleaner  
  
RUN chmod +x /usr/local/bin/rtcleaner  
  
VOLUME /data  
  
CMD ["/usr/local/bin/rtcleaner"]

