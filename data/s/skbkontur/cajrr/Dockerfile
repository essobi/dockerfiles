FROM maven:onbuild-alpine  
  
RUN apk add --no-cache tzdata  
  
ENV TZ=UTC  
  
EXPOSE 8080  
EXPOSE 8081  
CMD ["./docker-entrypoint.sh"]  

