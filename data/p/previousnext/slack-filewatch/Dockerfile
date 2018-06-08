FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates  
  
ADD slack-filewatch /slack-filewatch  
  
CMD ["/slack-filewatch"]  

