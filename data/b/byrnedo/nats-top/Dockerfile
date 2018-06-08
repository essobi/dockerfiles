FROM alpine:3.4  
ENV NATS_TOP_VERSION=v0.2.0  
# Forgive me for the --no-check-certificate  
RUN apk update && apk add --no-cache wget unzip && cd /tmp && \  
wget --no-check-certificate https://github.com/nats-io/nats-
top/releases/download/${NATS_TOP_VERSION}/nats-top-linux_amd64.zip && \  
unzip nats-top-linux_amd64.zip && \  
mv nats-top-linux_amd64/nats-top /usr/local/bin/nats-top  
  
ENTRYPOINT [ "/usr/local/bin/nats-top" ]  
CMD []  

