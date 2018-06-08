FROM alpine:3.5  
  
MAINTAINER sinnerliu  
  
RUN apk update && \  
apk add \--no-cache --update bash && \  
mkdir -p /conf && \  
mkdir -p /conf-copy && \  
apk add \--no-cache --update aria2 && \  
apk add git && \  
git clone https://github.com/sinnerliu/yaaw-zh /aria2-webui && \  
mkdir -p /aria2-webui/data/dl && \  
apk add \--update darkhttpd  
  
ADD files/start.sh /conf-copy/start.sh  
ADD files/aria2.conf /conf-copy/aria2.conf  
ADD files/on-complete.sh /conf-copy/on-complete.sh  
  
RUN chmod +x /conf-copy/start.sh  
  
WORKDIR /  
  
EXPOSE 6800  
EXPOSE 80  
  
  
  
CMD ["/conf-copy/start.sh"]  

