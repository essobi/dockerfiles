FROM alpine:3.6  
MAINTAINER Ryoga Saito proelbtn  
  
RUN apk --update add jq && rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh entrypoint.sh  
COPY introduce.json introduce.json  
  
ENTRYPOINT ["sh", "entrypoint.sh"]  
CMD ["."]  

