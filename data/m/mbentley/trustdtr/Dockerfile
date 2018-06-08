FROM alpine:latest  
MAINTAINER Matt Bentley <matt.bentley@docker.com>  
  
RUN apk --no-cache add curl openssl  
  
COPY trustdtr.sh /trustdtr.sh  
  
ENTRYPOINT ["/trustdtr.sh"]  
CMD ["--help"]  

