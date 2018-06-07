  
FROM alpine:latest  
MAINTAINER Matt Haught <matt@haught.org>  
  
RUN apk add --no-cache curl  
  
RUN mkdir -p /opt/hdhomerun \  
/opt/hdhomerun/bin \  
/opt/hdhomerun/etc  
  
RUN curl -o /opt/hdhomerun/bin/hdhomerun_record \  
-SL https://download.silicondust.com/hdhomerun/hdhomerun_record_linux  
  
RUN chmod 755 /opt/hdhomerun/bin/hdhomerun_record  
  
ADD hdhomerun.conf /opt/hdhomerun/etc/  
  
EXPOSE 65001/udp 65002  
VOLUME ["/data"]  
  
CMD ["/opt/hdhomerun/bin/hdhomerun_record", "foreground", "--conf",
"/opt/hdhomerun/etc/hdhomerun.conf"]  

