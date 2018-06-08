FROM alpine:3.6  
MAINTAINER nownabe <nownabe@gmail.com>  
  
RUN apk --update --no-cache add minidlna \  
&& mkdir -p /opt \  
&& chown minidlna. /opt  
  
ADD minidlna.conf /etc/minidlna.conf  
  
CMD minidlnad -d  

