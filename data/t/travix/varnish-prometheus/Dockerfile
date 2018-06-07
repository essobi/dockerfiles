FROM travix/varnish:4.1.2-r3  
  
MAINTAINER Travix  
  
ENV PROMETHEUS_VARNISH_EXPORTER_VERSION=1.1  
RUN apk --update add --virtual build-dependencies curl \  
&& apk add supervisor \  
&& rm -rf /var/cache/apk/*  
  
RUN curl -L
https://github.com/jonnenauha/prometheus_varnish_exporter/releases/download/${PROMETHEUS_VARNISH_EXPORTER_VERSION}/linux-
amd64.tar.gz | tar -xz -C /usr/bin \  
&& chmod +x /usr/bin/prometheus_varnish_exporter \  
&& mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
COPY start.sh /root  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN apk del build-dependencies  
  
CMD ["/usr/bin/supervisord"]  

