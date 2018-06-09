FROM docker:1.10  
RUN apk --update add bash tzdata apk-cron && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
echo "Asia/Tokyo" > /etc/timezone  
  
COPY .docker /root/.docker/  
  
COPY cron-entrypoint.sh /usr/local/bin/  
COPY backup /usr/local/bin/  
COPY restore /usr/local/bin/  
  
ENTRYPOINT ["cron-entrypoint.sh"]  

