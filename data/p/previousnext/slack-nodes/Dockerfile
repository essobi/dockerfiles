FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates  
  
ADD slack-nodes /slack-nodes  
RUN chmod a+x /slack-nodes  
  
CMD ["/slack-nodes"]  

