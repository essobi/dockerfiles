#  
# grafana  
#  
# Pull base image.  
FROM ashangit/base:latest  
MAINTAINER Nicolas Fraison <nfraison@yahoo.fr>  
  
ENV GRAFANA_VERSION 2.6.0-1  
# Deploy grafana.  
RUN yum install
https://grafanarel.s3.amazonaws.com/builds/grafana-${GRAFANA_VERSION}.x86_64.rpm
-y  
  
# Create required folders  
RUN mkdir -p /data/grafana/conf && \  
mkdir -p /data/grafana/data && \  
mkdir -p /data/grafana/db  
  
# Set working directory  
WORKDIR /usr/share/grafana  
  
# Copy default config file  
COPY conf/grafana.ini /data/grafana/conf/grafana.ini  
  
# Declare default env variables  
ENV GF_SECURITY_ADMIN_PASSWORD Adm1nTest  
  
# Expose grafana port  
EXPOSE 3000  
# Default command  
CMD grafana-server --config=/data/grafana/conf/grafana.ini
cfg:default.paths.data=/data/grafana/data

