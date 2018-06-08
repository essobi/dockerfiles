FROM alpine:3.6  
ENV NATSS_VERSION v0.6.0  
RUN apk update && \  
apk add --no-cache ca-certificates openssl  
  
RUN wget -q https://github.com/nats-io/nats-streaming-
server/releases/download/${NATSS_VERSION}/nats-streaming-
server-${NATSS_VERSION}-linux-amd64.zip -O /tmp/nats-streaming-server.zip && \  
unzip /tmp/nats-streaming-server.zip -d / && \  
mv /nats-streaming-server-${NATSS_VERSION}-linux-amd64/nats-streaming-server /
&& \  
rm /tmp/nats-streaming-server.zip  
  
RUN chmod +x /nats-streaming-server  
  
RUN mkdir -p /data/nats-streaming/  
  
# Expose client and management ports  
EXPOSE 4222 8222  
# Run with default memory based store  
#ENTRYPOINT ["/nats-streaming-server"]  

