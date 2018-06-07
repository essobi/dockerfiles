FROM alpine:3.3  
ENV DRIVER=digitalocean \  
COMMAND=create \  
VMNAME=default  
  
RUN apk --update add curl && \  
curl -L https://github.com/docker/machine/releases/download/v0.7.0/docker-
machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine && \  
apk del --purge curl && \  
rm -rf /var/cache/apk/*  
  
COPY ./ /  
  
CMD ["/bin/sh", "/entry.sh"]  

