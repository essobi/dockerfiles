FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN apk --no-cache add bind-tools  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

