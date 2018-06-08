FROM quay.io/justcontainers/base-alpine:latest  
MAINTAINER Ben Pye <ben@curlybracket.co.uk>  
  
ENV murmurversion=1.2.12  
ENV dockerizeversion=0.0.4  
RUN mkdir -p /opt/  
  
# Download statically compiled murmur and install it to /opt/murmur  
ADD https://github.com/mumble-
voip/mumble/releases/download/${murmurversion}/murmur-
static_x86-${murmurversion}.tar.bz2 /tmp/  
RUN tar -C /tmp -xjvf /tmp/murmur-static_x86-${murmurversion}.tar.bz2 && \  
mv /tmp/murmur-static_x86-${murmurversion} /opt/murmur  
  
# Download dockerize and install it to /usr/local/bin/  
ADD
https://github.com/jwilder/dockerize/releases/download/v${dockerizeversion}/dockerize-
linux-amd64-v${dockerizeversion}.tar.gz /tmp/  
RUN tar -C /usr/local/bin/ -xzvf /tmp/dockerize-linux-
amd64-v${dockerizeversion}.tar.gz  
  
# Download GTMurmur and install it to /usr/local/bin/  
ADD https://s.paste.ninja/1.2.0-bin.zip /tmp/  
RUN unzip /tmp/1.2.0-bin.zip -d /tmp/ && \  
mv /tmp/1.2.0/gtmurmur-static /usr/local/bin/ && \  
chmod +x /usr/local/bin/gtmurmur-static  
  
# Install inotify-tools  
RUN apk update && apk add inotify-tools  
  
ADD services.d /etc/services.d/  
ADD cont-init.d /etc/cont-init.d/  
  
ADD murmur.tmpl /etc/murmur.tmpl  
  
RUN rm -rf /tmp/*  
  
# Expose apporpriate ports  
EXPOSE 64738/tcp 64738/udp 27800/tcp 27800/udp  
  
# Read murmur.sqlite from /data, certificates from /certs  
VOLUME ["/data", "/certs"]  
  
# Run s6  
ENTRYPOINT ["/init"]  

