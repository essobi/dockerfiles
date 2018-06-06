FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates  
  
ADD cleanup-jobs /cleanup-jobs  
RUN chmod a+x /cleanup-jobs  
  
CMD ["/cleanup-jobs"]  

