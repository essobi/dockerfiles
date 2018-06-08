FROM alpine:3.7  
RUN apk add --no-cache curl  
  
ENTRYPOINT ["/usr/bin/curl", "http://169.254.169.254/latest/meta-
data/iam/security-credentials/"]  

