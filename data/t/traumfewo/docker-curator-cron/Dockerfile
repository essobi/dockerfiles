FROM alpine:3.5  
RUN apk --update add python py-pip curl && \  
pip install elasticsearch-curator==5.0.1 && \  
mkdir -p /root/.curator/  
  
COPY ./bin /usr/local/bin  
COPY curator.yml /root/.curator/  
  
ENTRYPOINT ["/usr/local/bin/curator-cron"]  

