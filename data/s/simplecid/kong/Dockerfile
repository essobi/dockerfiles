ARG VERSION=0.13.0  
FROM kong:$VERSION  
  
RUN apk --no-cache add git  
  
COPY entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

