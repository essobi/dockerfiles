FROM mikroways/rsnapshot:latest  
MAINTAINER Mikroways <christian.rodriguez@mikroways.net>  
  
RUN apk --no-cache -U add curl  
COPY docker-entrypoint-rancher.sh /docker-entrypoint-rancher.sh  
RUN chmod +x /docker-entrypoint-rancher.sh  
ENTRYPOINT ["/docker-entrypoint-rancher.sh"]  
CMD ["backup"]  

