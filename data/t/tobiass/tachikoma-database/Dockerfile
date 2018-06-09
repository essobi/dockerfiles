FROM ubuntu:17.10  
LABEL maintainer="tachikoma@sourceforgery.com"  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y --no-install-recommends install rabbitmq-server postgresql-
contrib-9.6 postgresql-9.6 postgresql-client-9.6 sudo dirmngr && \  
rm -rf /var/cache/apt/ /var/lib/apt/lists/*  
  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc
/tini.asc  
  
RUN gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --verify /tini.asc  
  
RUN chmod +x /tini  
  
ENTRYPOINT ["/tini", "--"]  
  
ADD /conf/rabbitmq/* /etc/rabbitmq/  
ADD /conf/start.sh /  
ADD /conf/patch_pg_conf.sh /etc/postgresql/  
  
RUN /etc/postgresql/patch_pg_conf.sh  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
  
# PostgreSQL  
EXPOSE 5432  
# RabbitMQ  
EXPOSE 5672  
# RabbitMQ management plugin web interface  
EXPOSE 15672  
CMD ["/start.sh"]  

