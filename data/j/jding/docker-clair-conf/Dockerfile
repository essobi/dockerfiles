FROM alpine:3.7 as builder  
  
RUN apk add --update curl && \  
mkdir -p /config && \  
curl -Ssl
https://raw.githubusercontent.com/coreos/clair/master/config.yaml.sample > \  
/config/config.yaml  
  
FROM alpine:3.7  
COPY docker-entrypoint.sh /  
COPY \--from=builder /config/config.yaml /config/config.yaml  
  
VOLUME /config  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

