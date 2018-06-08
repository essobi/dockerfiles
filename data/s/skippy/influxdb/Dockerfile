FROM tutum/influxdb:latest  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
ADD config.toml /config/config.toml  
ADD collectd_types.db /config/collectd_types.db  
#ADD shardSpace.json /config/shardSpace.json  
# Raft port (for clustering, don't expose publicly!)  
EXPOSE 8090  
# Protobuf port (for clustering, don't expose publicly!)  
EXPOSE 8099  
# CollectD endpoint  
EXPOSE 25826/udp  
  
#ADD run.sh /run.sh  
#RUN chmod +x /run.sh  
#CMD ["/run.sh"]

