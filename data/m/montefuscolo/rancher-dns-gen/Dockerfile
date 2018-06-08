FROM alpine:edge  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@gmail.com>  
  
ENV LOG_LEVEL="info"  
ARG VERSION_RANCHER_GEN="artifacts/master"  
ARG VERSION_FOREGO="v0.16.1"  
RUN apk add --no-cache bash bind-tools curl dnsmasq supervisor unzip \  
&& curl -s -L "https://gitlab.com/adi90x/rancher-gen-
rap/-/jobs/$VERSION_RANCHER_GEN/download?job=compile-go" -o /tmp/rancher-gen-
rap.zip \  
&& unzip /tmp/rancher-gen-rap.zip -d /usr/local/bin \  
&& rm -f /tmp/rancher-gen-rap.zip \  
&& chmod +x /usr/local/bin/rancher-gen  
  
COPY /app /app  
WORKDIR /app  
  
EXPOSE 53 53/udp  
ENTRYPOINT ["/app/entrypoint.sh"]  
CMD ["supervisord", "-n", "-c", "/app/supervisor.conf", "-l", "/dev/stdout"]  

