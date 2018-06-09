FROM alpine:latest  
MAINTAINER Simon Jagoe <simon@scalative.com>  
ENV JQ_VERSION=1.5  
RUN apk update && \  
apk add --no-cache --update-cache curl bash && \  
curl -o /usr/local/bin/jq -L
https://github.com/stedolan/jq/releases/download/jq-$JQ_VERSION/jq-linux64 &&
\  
chmod +x /usr/local/bin/jq  
VOLUME ["/data"]  
WORKDIR /data  
ENTRYPOINT ["/usr/local/bin/jq"]  
CMD ["--help"]  

