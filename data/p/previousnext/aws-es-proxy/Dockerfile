FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates  
  
ADD aws-es-proxy-0.3 /usr/local/bin/aws-es-proxy  
RUN chmod +rx /usr/local/bin/aws-es-proxy  
  
CMD ["aws-es-proxy"]  

