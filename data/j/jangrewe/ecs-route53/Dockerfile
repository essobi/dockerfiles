FROM alpine:latest  
  
ENV CLI53_VERSION 0.7.4  
ADD update.sh /bin/update.sh  
ADD
https://github.com/barnybug/cli53/releases/download/${CLI53_VERSION}/cli53-linux-386
/bin/cli53  
RUN chmod +x /bin/update.sh /bin/cli53 && \  
apk add --no-cache bash openssl ca-certificates  
ENTRYPOINT ["/bin/update.sh"]  

