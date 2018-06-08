FROM alpine:latest  
  
MAINTAINER Ilya Stepanov <dev@ilyastepanov.com>  
  
RUN apk add --no-cache bash  
  
ADD entrypoint.sh /entrypoint.sh  
ADD onstart.sh /onstart.sh  
ADD onfinish.sh /onfinish.sh  
RUN chmod +x /entrypoint.sh && \  
chmod +x /onstart.sh && \  
chmod +x /onfinish.sh  
  
ADD command.sh /command.sh  
RUN chmod +x /command.sh  
  
ONBUILD ADD command.sh /command.sh  
ONBUILD RUN chmod +x /command.sh  
  
ENV CRON_SCHEDULE '0 1 * * *'  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

