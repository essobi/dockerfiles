FROM alpine:3.5  
EXPOSE 6419  
WORKDIR /data  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
RUN apk --no-cache add py2-pip  
  
RUN pip install --no-cache-dir grip  
  
ADD docker-entrypoint.sh /bin/docker-entrypoint.sh  

