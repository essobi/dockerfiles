FROM alpine:latest  
  
  
RUN apk --update add python py-pip && \  
pip install elasticsearch-curator && \  
pip install requests-aws4auth && \  
rm -rf /var/cache/apk/*  
  
ADD entrypoint.sh /entrypoint.sh  
  
WORKDIR /usr/share/curator  
COPY config ./config  
  
RUN chmod +x /entrypoint.sh  
  
#run every minute  
ENV CRON */1 * * * *  
ENV ES_HOST 127.0.0.1  
ENV CONFIG_FILE /usr/share/curator/config/curator.yml  
ENV COMMAND /usr/share/curator/config/delete_log_files_curator.yml  
  
ENTRYPOINT ["/entrypoint.sh"]  

