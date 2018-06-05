FROM alpine:edge  
  
MAINTAINER riverscn <riverscn@gmail.com>  
  
RUN apk update && \  
apk add \--no-cache --update bash && \  
mkdir -p /conf && \  
mkdir -p /conf-copy && \  
mkdir -p /data && \  
apk add \--no-cache --update aria2  
  
ADD files/start.sh /conf-copy/start.sh  
ADD files/aria2.conf /conf-copy/aria2.conf  
ADD files/on-complete.sh /conf-copy/on-complete.sh  
  
RUN chmod +x /conf-copy/start.sh  
  
WORKDIR /  
VOLUME ["/data"]  
VOLUME ["/conf"]  
EXPOSE 6800  
  
CMD ["/conf-copy/start.sh"]  

