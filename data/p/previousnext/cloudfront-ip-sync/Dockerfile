FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates  
  
ADD cloudfront-ip-sync /cloudfront-ip-sync  
RUN chmod a+x /cloudfront-ip-sync  
  
CMD ["/cloudfront-ip-sync"]  

