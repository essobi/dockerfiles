FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates  
  
ADD slack-restarts /slack-restarts  
RUN chmod a+x /slack-restarts  
  
CMD ["/slack-restarts"]  

