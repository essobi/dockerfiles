FROM alpine:edge  
WORKDIR /root/  
RUN apk add --update-cache imapfilter  
COPY crontab /var/spool/cron/crontabs/root  
VOLUME /root/.imapfilter  
CMD ["crond", "-f", "-l", "0", "-d", "0"]  

