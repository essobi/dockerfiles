FROM alpine:latest  
  
MAINTAINER Jens Piegsa <piegsa@gmail.com>  
  
ENV DAYS 3650  
COPY entry.sh /entry.sh  
  
RUN apk add --no-cache openssl && \  
chmod +x /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  

