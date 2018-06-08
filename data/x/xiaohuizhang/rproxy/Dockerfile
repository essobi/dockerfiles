FROM alpine:3.5  
ENV PEN_VERSION="0.34.1"  
RUN apk --update add alpine-sdk  
RUN wget -q "http://siag.nu/pub/pen/pen-$PEN_VERSION.tar.gz" -P /tmp && \  
tar xfz "/tmp/pen-$PEN_VERSION.tar.gz" -C / && \  
cd "/pen-$PEN_VERSION" && \  
./configure && \  
make && \  
make install  
RUN apk del alpine-sdk  
  
RUN mkdir /etc/pen/  
# pen-starter  
# /usr/local/bin/pen -f -S $(grep '^server' servers|wc -l) $@ -F
/etc/pen/servers 8080  
ADD pen-starter /usr/local/bin/pen-starter  
RUN chmod 755 /usr/local/bin/pen-starter  
ADD servers /etc/pen/servers  
EXPOSE 8080  
ENTRYPOINT ["/usr/local/bin/pen-starter"]  

