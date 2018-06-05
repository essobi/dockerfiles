FROM bytesized/debian-base  
MAINTAINER maran@bytesized-hosting.com  
  
ADD https://download-cdn.resilio.com/2.4.1/linux-x64/resilio-sync_x64.tar.gz
/tmp/sync.tgz  
RUN mkdir -p /app && tar -xf /tmp/sync.tgz -C /app/ rslsync && rm -f
/tmp/sync.tgz  
  
VOLUME /config /data /media  
  
COPY /static /  
  
EXPOSE 8888 55555  

