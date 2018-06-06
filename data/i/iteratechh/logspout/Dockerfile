FROM gliderlabs/logspout:master  
  
ENV DOCKERIZE_VERSION v0.3.0  
ENV KAFKA_COMPRESSION_CODEC snappy  
  
# Prepare SSL functionality for wget HTTPS  
RUN apk update && \  
apk add ca-certificates wget && \  
update-ca-certificates  
  
# Get dockerize  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Wait for target logstash  
# CMD dockerize -wait tcp $(echo $ROUTE_URIS | grep -Eo '(tcp|udp).*$')

