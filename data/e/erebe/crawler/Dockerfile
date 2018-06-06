FROM alpine:latest  
MAINTAINER github@erebe.eu  
  
  
RUN adduser -D crawler  
ADD
https://github.com/erebe/crawler/releases/download/1.1/crawler.tar.gz?raw=true
/home/crawler/  
ADD run.sh /home/crawler/  
RUN cd /home/crawler && \  
tar xzvf crawler.tar.gz && \  
rm crawler.tar.gz && \  
apk update && \  
apk add ca-certificates && \  
rm -rf /var/cache/apk/*  
  
USER crawler  
WORKDIR /home/crawler  
  
VOLUME /data  
ENV SLEEP_TIME_SEC 1800  
CMD ["./run.sh"]  
  

