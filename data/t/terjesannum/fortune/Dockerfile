FROM alpine:3.5  
LABEL maintainer "terje@offpiste.org"  
  
RUN apk add --no-cache fortune  
  
COPY loop.sh /  
CMD ["/loop.sh"]  

