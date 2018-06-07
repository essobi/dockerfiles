FROM alpine:latest  
RUN apk add --update openssl  
  
RUN mkdir /app  
WORKDIR /app  
RUN wget -O fileserve
https://github.com/greinacker/fileserve/releases/download/v0.2.1/fileserve-
amd64 \  
&& chmod 755 /app/fileserve  
  
CMD "/app/fileserve"  

