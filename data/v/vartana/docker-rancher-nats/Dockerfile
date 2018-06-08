FROM debian:jessie-backports  
  
MAINTAINER Derek Collison <derek@apcera.com>  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD gnatsd /gnatsd  
  
RUN chmod +x /gnatsd  
  
ADD gnatsd.conf /gnatsd.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENV RANCHER_ENABLE=  
ENV NATS_USER=  
ENV NATS_PASS=  
ENV NATS_CLUSTER_USER=ruser  
ENV NATS_CLUSTER_PASS=T0pS3cr3t  
ENV NATS_CLUSTER_ROUTES=  
  
# Expose client, management, and routing/cluster ports  
EXPOSE 4222 8222 6222  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/gnatsd", "-c", "/gnatsd.conf"]  

