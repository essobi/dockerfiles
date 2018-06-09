FROM openjdk:alpine  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENV TZ=Europe/Moscow  
  
RUN apk add -U tzdata  
  
RUN rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/entrypoint.sh"]

