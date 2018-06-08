FROM debian:jessie  
  
ENV SENSU_RABBITMQ_HOST localhost  
ENV SENSU_RABBITMQ_VHOST /  
ENV SENSU_RABBITMQ_USER guest  
ENV SENSU_RABBITMQ_PASSWORD guest  
ENV SENSU_REDIS_HOST localhost  
ENV SENSU_API_PORT 4567  
ENV SENSU_ROLE server  
  
ADD http://repos.sensuapp.org/apt/pubkey.gpg /sensu_key.gpg  
RUN apt-key add sensu_key.gpg  
RUN echo "deb http://repos.sensuapp.org/apt sensu main" >>
/etc/apt/sources.list.d/sensu.list  
RUN apt-get update && apt-get install -y sensu  
COPY docker-entrypoint.sh /entrypoint.sh  
ADD https://github.com/groob/sensu-config/releases/download/v0.0.5/sensu-
config.tar.gz /  
RUN tar -xvf /sensu-config.tar.gz  
ENTRYPOINT ["/entrypoint.sh"]  

