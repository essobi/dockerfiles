FROM alpine  
LABEL maintainer="Gildas Cherruel <gildas@breizh.org>"  
LABEL version="0.0.2"  
LABEL description="Runs rabbitmqadmin"  
  
ENV RABBITMQ_HOST localhost  
ENV RABBITMQ_PORT 15672  
ENV RABBITMQ_USER guest  
ENV RABBITMQ_PASSWORD guest  
ENV RABBITMQ_VHOST /  
  
RUN addgroup -S rabbitmq && \  
adduser -S -g rabbitmq rabbitmq  
  
RUN apk add --no-cache curl && \  
apk add --no-cache python && \  
curl -L https://raw.githubusercontent.com/rabbitmq/rabbitmq-
management/v3.7.4/bin/rabbitmqadmin -o /usr/bin/rabbitmqadmin && \  
chmod +x /usr/bin/rabbitmqadmin  
ADD ./runit /usr/bin  
RUN chmod +x /usr/bin/runit  
  
USER rabbitmq  
  
ENTRYPOINT [ "/usr/bin/runit" ]  
CMD [ "" ]  

