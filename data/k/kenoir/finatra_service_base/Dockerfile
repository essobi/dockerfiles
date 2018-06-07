FROM anapsix/alpine-java  
  
RUN apk update && apk add gettext && rm -rf /var/cache/apk  
  
RUN mkdir -p /opt/docker  
  
COPY run.sh /run.sh  
  
EXPOSE 8888  

