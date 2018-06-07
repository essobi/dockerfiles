FROM alpine:3.2  
MAINTAINER Jasper Lievisse Adriaanse <j@jasper.la>  
  
RUN apk add --update darkhttpd && rm -rf /var/cache/apk/*  
  
ADD run.sh /  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  

