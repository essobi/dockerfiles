FROM alpine:3.3  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
COPY run.sh /bin/run.sh  
RUN apk --no-cache add \  
socat && \  
chmod +x /bin/run.sh  
  
ENTRYPOINT ["/bin/run.sh"]  

