FROM alpine  
  
RUN apk --update upgrade && apk add curl ca-certificates docker openssh && rm
-rf /var/cache/apk/*  
  
ENV ENV 1a5  
ENV URL ''  
ENV ACCESS_KEY ''  
ENV SECRET_KEY ''  
ADD docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENV CLI_VERSION=v0.6.4 \  
COMPOSE_VERSION=v0.12.5  
ADD https://github.com/rancher/cli/releases/download/$CLI_VERSION/rancher-
linux-amd64-$CLI_VERSION.tar.gz /rancher.tar.gz  
ADD https://github.com/rancher/rancher-
compose/releases/download/$COMPOSE_VERSION/rancher-compose-linux-
amd64-$COMPOSE_VERSION.tar.gz /rancher-compose.tar.gz  
  
RUN tar -xf /rancher.tar.gz && \  
tar -xf /rancher-compose.tar.gz  
  
RUN mv /rancher-$CLI_VERSION/rancher /bin/ && \  
mv /rancher-compose-$COMPOSE_VERSION/rancher-compose /bin/  
  
RUN adduser -S docker-user  
USER docker-user  
ENTRYPOINT ["/docker-entrypoint.sh"]  

