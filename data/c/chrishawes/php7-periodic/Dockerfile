FROM chrishawes/php7-cli  
  
RUN curl -L --insecure https://github.com/odise/go-
cron/releases/download/v0.0.7/go-cron-linux.gz | zcat > /usr/local/bin/go-cron
&& \  
chmod u+x /usr/local/bin/go-cron  
  
ENV SCHEDULE None  
ENV PORT 8080  
ENV COMMAND None  
  
EXPOSE 8080  
ADD run.sh run.sh  
  
ENTRYPOINT ["sh", "run.sh"]  

