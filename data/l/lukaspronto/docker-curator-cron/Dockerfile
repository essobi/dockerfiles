FROM alpine:3.2  
RUN apk --update add python py-pip && \  
pip install elasticsearch-curator==3.4.0  
  
COPY ./bin /usr/local/bin  
RUN chmod +x /usr/local/bin/curator-cron  
  
ENTRYPOINT ["/usr/local/bin/curator-cron"]  

