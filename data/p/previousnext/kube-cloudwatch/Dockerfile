FROM gliderlabs/alpine:3.1  
MAINTAINER Nick Schuch  
  
RUN apk --update add ca-certificates  
  
ADD kube-cloudwatch-linux-amd64 /kube-cloudwatch  
  
CMD ["/kube-cloudwatch"]  

