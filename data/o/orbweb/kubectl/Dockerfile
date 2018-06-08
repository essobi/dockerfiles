FROM alpine:3.3  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
ENV VERSION 1.2.2  
RUN apk --no-cache add --virtual .build-deps curl && \  
curl https://storage.googleapis.com/kubernetes-
release/release/v$VERSION/bin/linux/amd64/kubectl > /usr/local/bin/kubectl &&
\  
chmod +x /usr/local/bin/kubectl && \  
apk del .build-deps  
WORKDIR /root  
ENTRYPOINT ["/bin/sh"]  
# CMD ["kubectl", "-h"]  

