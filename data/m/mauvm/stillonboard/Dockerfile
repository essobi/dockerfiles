FROM alpine:3.3  
MAINTAINER Maurits van Mastrigt <maurits@nerdieworks.nl>  
  
RUN apk add --update bash socat jq \  
&& rm -rf /var/cache/apk/*  
  
COPY serve.sh /serve  
RUN chmod +x /serve  
  
EXPOSE 8080  
CMD socat tcp-l:8080,reuseaddr,fork EXEC:/serve  

