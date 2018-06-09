FROM alpine:3.2  
MAINTAINER Eagle Liut <eagle@dantin.me>  
  
RUN apk add --update darkhttpd && rm -rf /var/cache/apk/*  
  
RUN mkdir /htdocs  
  
VOLUME /htdocs  
  
EXPOSE 80  
CMD ["/usr/bin/darkhttpd", "/htdocs", "--port", "80"]  

