FROM alpine:latest  
  
MAINTAINER xujinkai <jack777@xujinkai.net>  
  
RUN apk update && \  
apk add \--no-cache --update bash && \  
mkdir -p /config && \  
mkdir -p /config-copy && \  
mkdir -p /data && \  
apk add \--no-cache --update aria2 && \  
apk add git && \  
git clone https://github.com/ziahamza/webui-aria2 /aria2-webui && \  
rm /aria2-webui/.git* -rf && \  
apk del git && \  
apk add \--update darkhttpd  
  
ADD files/start.sh /config-copy/start.sh  
ADD files/aria2.conf /config-copy/aria2.conf  
ADD files/on-complete.sh /config-copy/on-complete.sh  
  
RUN chmod +x /config-copy/start.sh  
  
WORKDIR /  
VOLUME ["/data"]  
VOLUME ["/config"]  
EXPOSE 6800  
EXPOSE 80  
EXPOSE 8080  
  
CMD ["/config-copy/start.sh"]  

