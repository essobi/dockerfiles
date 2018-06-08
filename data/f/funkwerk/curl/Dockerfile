FROM alpine:3.4  
MAINTAINER think@hotmail.de  
RUN apk add --update curl && rm -rf /var/cache/apk/*  
ENTRYPOINT ["curl"]  
CMD ["--help"]  

