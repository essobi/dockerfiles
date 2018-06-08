FROM alpine:latest  
  
RUN apk --no-cache add --update curl ca-certificates && update-ca-certificates  
RUN curl -o /etc/mime.types
https://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types  
RUN curl -o /tmp/otaru-bin.tar.gz https://storage.googleapis.com/otaru-
release/otaru-bin.tar.gz \  
&& mkdir -p /opt/otaru && tar zxf /tmp/otaru-bin.tar.gz -C /opt/otaru && rm -f
/tmp/* \  
&& mkdir -p /etc/otaru && mkdir -p /var/cache/otaru  
ENV OTARUDIR=/etc/otaru  
VOLUME ["/etc/otaru", "/var/cache/otaru"]  
EXPOSE 10246 8005  
ENTRYPOINT ["/opt/otaru/otaru-bin/otaru-proxy"]  

