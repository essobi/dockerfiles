FROM alpine:3.4  
MAINTAINER Adam White <adam@whiteadam.com>  
  
RUN apk add curl --no-cache  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["curl"]  

