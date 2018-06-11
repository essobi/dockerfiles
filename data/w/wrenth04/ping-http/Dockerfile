FROM alpine:3.3  
MAINTAINER Phil Huang <wrenth04@gmail.com>  
RUN apk add --update curl  
ENV URI=https://blog-wrenth04.rhcloud.com \  
DELAY=60  
COPY start /  
CMD ["./start"]  

