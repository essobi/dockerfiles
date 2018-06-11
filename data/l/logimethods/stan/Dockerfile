#FROM scratch  
# https://github.com/docker/docker/issues/23865  
FROM alpine:latest  
  
COPY nats-streaming-server-linux-386/nats-streaming-server /nats-streaming-
server  
COPY nats-streaming-server.conf /nats-streaming-server.conf  
  
# Expose client, management, and cluster ports  
EXPOSE 4222 8222 6222  
# Run via the configuration file  
ENTRYPOINT ["/nats-streaming-server", "-c", "/nats-streaming-server.conf"]  
CMD []  

