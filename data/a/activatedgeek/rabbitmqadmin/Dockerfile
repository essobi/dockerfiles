FROM alpine:latest  
  
MAINTAINER Sanyam Kapoor "1sanyamkapoor@gmail.com"  
ADD ./scripts/docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN apk update &&\  
apk add --update curl python &&\  
curl https://raw.githubusercontent.com/rabbitmq/rabbitmq-
management/rabbitmq_v3_6_1/bin/rabbitmqadmin -o /usr/bin/rabbitmqadmin &&\  
chmod +x /usr/bin/rabbitmqadmin &&\  
chmod +x /docker-entrypoint.sh  
  
# possible environment variables with defaults  
ENV RABBIT_HOST=127.0.0.1 \  
RABBIT_PORT=15672 \  
RABBIT_USER=guest \  
RABBIT_PASSWORD=guest \  
RABBIT_VHOST=/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

