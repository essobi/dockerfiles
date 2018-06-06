FROM gganssauge/fluent-bit-arm:0.11.3  
MAINTAINER Gottfried Ganßauge <ganssauge@gmx.de>  
USER root  
  
COPY fluent-bit.conf /fluent-bit/etc/  
COPY parsers.conf /fluent-bit/etc/  
  
CMD ["/fluent-bit/bin/fluent-bit", "-c", "/fluent-bit/etc/fluent-bit.conf"]  

