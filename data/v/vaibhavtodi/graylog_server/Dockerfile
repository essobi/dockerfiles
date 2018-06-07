# Specifing the base image  
FROM vaibhavtodi/java:1.0  
  
# Maintainer  
MAINTAINER "Vaibhav Todi" <vaibhavtodi1989@gmail.com>  
  
# Specifing the Label  
LABEL Description="DOCKER IMAGE WHERE GRAYLOG-SERVER IS SETUP" \  
Version="1.3"  
  
# Setting the ENV variable  
ENV JAVA /usr/lib/jvm/java-7-oracle  
  
# Downloading & Installing the Graylog-Server  
RUN wget https://packages.graylog2.org/repo/packages/graylog-1.3-repository-
ubuntu14.04_latest.deb \  
&& dpkg -i graylog-1.3-repository-ubuntu14.04_latest.deb \  
&& apt-get update \  
&& apt-get install -y graylog-server \  
&& rm -f graylog-1.3-repository-ubuntu14.04_latest.deb  
  
# Copying the Graylog Server configuration file  
COPY server.conf /etc/graylog/server/server.conf  
  
# Copying the entrypoint.sh for running the service  
COPY entrypoint.sh /entrypoint.sh  
  
# Setting up the Graylog Server Configuration  
RUN sed -i 's/gs_master/true/' /etc/graylog/server/server.conf \  
&& sed -i
's/gs_password_secret/lGOVlXDzWwfkvyjwiYgN11ASGxBJpX0VWpLTiDrDVfOHdx2nOa3bplnNTHt1hx8PRfs2CjAfrlwPFBHHwrJFPNVTTjeUS9qZ/'
/etc/graylog/server/server.conf \  
&& sed -i 's/gs_username/admin/' /etc/graylog/server/server.conf \  
&& sed -i
's/gs_password_sha/8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918/'
/etc/graylog/server/server.conf \  
&& sed -i 's/gs_root_email/"vaibhavtodi1989@gmail.com"/'
/etc/graylog/server/server.conf \  
&& sed -i 's/gs_timezone/UTC/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_rest_listen_uri/http:\/\/0\\.0\\.0\\.0:12900\//'
/etc/graylog/server/server.conf \  
&& sed -i 's/gs_rest_transport_uri/http:\/\/0\\.0\\.0\\.0:12900\//'
/etc/graylog/server/server.conf \  
&& sed -i 's/gs_rest_enable_cors/false/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_no_retention/true/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_retention_strategy/delete/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_max_no_indices/20/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_shards/4/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_replicas/1/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_index_prefix/testing/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_cluster_name/graylog/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_node_master/false/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_node_data/false/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_transport_tcp_port/9350/' /etc/graylog/server/server.conf \  
&& sed -i 's/gs_unicast/172\\.17\\.0\\.1:9300/'
/etc/graylog/server/server.conf \  
&& sed -i 's/gs_mongodb_uri/mongodb:\/\/172\\.17\\.0\\.1:27017\/graylog2/'
/etc/graylog/server/server.conf  
  
# Cleaning the Docker image  
RUN apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/*  
  
# Exposing the Ports  
EXPOSE 12900 \  
443 443/udp \  
12201 12201/udp \  
514 514/udp  
  
# Mounting the Volumes  
VOLUME ["/var/log/graylog-server", "/etc/graylog"]  
  
# Specifing the CMD instruction  
CMD ["/entrypoint.sh"]  

