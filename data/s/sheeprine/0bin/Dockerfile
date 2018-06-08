FROM alpine:latest  
MAINTAINER Stephane Albert "sheeprine@nullplace.com"  
ENV HOST 0.0.0.0  
ENV PORT 8000  
RUN apk add --no-cache python3 && rm -rf /var/cache/apk/*  
RUN pip3 install zerobin  
ADD entrypoint.sh /  
  
ENTRYPOINT ["./entrypoint.sh"]  

