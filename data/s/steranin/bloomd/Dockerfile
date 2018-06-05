FROM alpine:3.4  
MAINTAINER steranin  
  
RUN apk add --update build-base scons git \  
&& git clone https://github.com/armon/bloomd /tmp/bloomd \  
&& cd /tmp/bloomd \  
&& git checkout 4659b3a0971e2f731a5c0830cee810d0dbe3eabb \  
&& scons \  
&& cp bloomd /usr/local/bin/bloomd \  
&& rm -rf /tmp/bloomd \  
&& apk del build-base scons git \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /data  
VOLUME /etc/bloomd  
  
ADD bloomd.conf /etc/bloomd/bloomd.conf  
  
EXPOSE 8673  
ENTRYPOINT ["/usr/local/bin/bloomd"]  
CMD ["-f", "/etc/bloomd/bloomd.conf"]  

