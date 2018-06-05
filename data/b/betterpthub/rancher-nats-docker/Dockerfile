FROM debian:jessie  
  
MAINTAINER Ruslan Sheremet <info.webstudio@gmail.com>  
  
RUN apt-get update \  
&& apt-get install curl locales -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV LANG en_US.utf8  
  
RUN mkdir -p /usr/local/nats  
  
ADD gnatsd /usr/local/nats/gnatsd  
ADD gnatsd.conf /usr/local/nats/gnatsd.conf  
ADD docker-entrypoint.sh /usr/local/nats/docker-entrypoint.sh  
RUN chmod 755 -R /usr/local/nats  
  
ENV RANCHER_ENABLE=  
ENV NATS_USER=  
ENV NATS_PASS=  
ENV NATS_CLUSTER_USER=ruser  
ENV NATS_CLUSTER_PASS=T0pS3cr3t  
ENV NATS_CLUSTER_ROUTES=  
  
# Expose client, management, and routing/cluster ports  
EXPOSE 4222 8222 6222  
ENTRYPOINT ["/usr/local/nats/docker-entrypoint.sh"]  
CMD ["/usr/local/nats/gnatsd", "-c", "/usr/local/nats/gnatsd.conf"]  

