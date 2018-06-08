FROM alpine:latest  
  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
ADD https://pagekite.net/pk/ /tmp/pagekite.install  
  
RUN apk --update add python bash curl && bash /tmp/pagekite.install && \  
apk del bash curl  
  
VOLUME /etc/pagekite.d  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/pagekite.py"]  

