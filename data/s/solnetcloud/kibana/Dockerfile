# Kibana Docker  
# Solnet Solutions  
# Version: 4.4.0  
  
# Pull base image (Ubuntu 14.04)  
FROM ubuntu:14.04  
  
# Build Instructions:  
# When building use the following flags  
# \--tag="kibana:4.4.0"  
  
# Run Instruction:  
# When running use the following flags:  
# \--restart=on-failure --log-driver=syslog  
# The following command line arguments are supported.  
# usage: entry [-h] [--kibana-index [KIBANA_INDEX]] [--kb-ssl-crt
[KB_SSL_CRT]]  
# [--kb-ssl-key [KB_SSL_KEY]] [--ignore-match-errors]  
# [--es-username [ES_USERNAME]] [--es-password [ES_PASSWORD]]  
# [--es-ssl-crt [ES_SSL_CRT]] [--es-ssl-key [ES_SSL_KEY]]  
# [--es-ssl-ca [ES_SSL_CA]] [--ignore-ssl]  
# es_url  
  
# positional arguments:  
# es_url The URL this container should use to access  
# Elasticsearch  
#  
# optional arguments:  
# -h, --help show this help message and exit  
# \--kibana-index [KIBANA_INDEX], -i [KIBANA_INDEX]  
# The index Kiabana should use for logstash indexing,  
# defaults to ".kibana"  
#  
# ssl:  
# Arguments for when you want Kibana to use SSL termination  
#  
# \--kb-ssl-crt [KB_SSL_CRT], -r [KB_SSL_CRT]  
# Certificate for SSL termination, under the /kb-  
# data/ssl/ volume  
# \--kb-ssl-key [KB_SSL_KEY], -k [KB_SSL_KEY]  
# SSL Key for SSL termination, under the /kb-data/ssl/  
# volume  
# \--ignore-match-errors  
# Ignore SSL certificate match errors. (Not recommended)  
#  
# credentials:  
# Arguments for when your ES instance has auth requirements  
#  
# \--es-username [ES_USERNAME], -u [ES_USERNAME]  
# Username for basic auth  
# \--es-password [ES_PASSWORD], -p [ES_PASSWORD]  
# Password for basic auth  
# \--es-ssl-crt [ES_SSL_CRT], -R [ES_SSL_CRT]  
# Certificate for client certificate authentication,  
# under the /kb-data/ssl/ volume  
# \--es-ssl-key [ES_SSL_KEY], -K [ES_SSL_KEY]  
# SSL Key for client certificate authentication, under  
# the /kb-data/ssl/ volume  
# \--es-ssl-ca [ES_SSL_CA], -C [ES_SSL_CA]  
# CA Certificate for SSL, under the /kb-data/ssl/ volume  
# \--ignore-ssl Ignore SSL Validation Errors. Will make --es-ssl-ca  
# redundant. (Testing)  
  
# Information  
MAINTAINER Taylor Bertie <taylor.bertie@solnet.co.nz>  
LABEL Description="This image is used to stand up an unsecured kibana
instance. Provide the elasticsearch URL as the \  
argument (no default; required) on startup" Version="4.4.0"  
  
# Patch notes:  
# Version 4.4.0  
# \- Updated Kibana to Version 4.4.0  
# Version 4.1.0  
# \- Updated Kibana to Version 4.1.0  
# Version 4.0.3  
# \- Updated Kibana to Version 4.0.3  
# Version 4.0.2-r2  
# \- Created a more generic template loader to be used in other entry scripts  
# \- Generalised the entry script  
# Version 4.0.2-r1  
# \- Moved kibana.yml to templates as it has a varible in it that is
maintained by the entry script.  
# \- Rewrote the entry script in python  
# Version 4.0.2:  
# \- First working version of Kibana  
  
# Set the Logstash Version and other enviroment variables-d  
ENV KB_PKG_NAME kibana-4.1.0-linux-x64  
  
# Install any required preqs  
RUN \  
apt-get update && \  
apt-get install wget python python-requests python-jinja2 python-openssl
python-crypto -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Prepare the various directories in /kb-data/  
RUN \  
mkdir -p /kb-data && \  
mkdir -p /kb-data/ssl && \  
mkdir -p /kb-templates  
  
# Install Kibana and delete the Kibana tarball  
RUN \  
cd / && \  
wget https://download.elastic.co/kibana/kibana/$KB_PKG_NAME.tar.gz && \  
tar xvzf $KB_PKG_NAME.tar.gz && \  
rm -f $KB_PKG_NAME.tar.gz && \  
mv /$KB_PKG_NAME /kibana && \  
rm /kibana/config/kibana.yml  
  
# Add volume for ssl client certificates  
VOLUME /kb-data/ssl/  
  
# Mount the configuration files, entry script and templates  
# Templates  
ADD templates/kibana.yml /kb-templates/kibana.yml  
  
# Configuration Files  
# None  
  
# Entry Script  
ADD scripts/entry.py /usr/local/bin/entry  
RUN chmod +x /usr/local/bin/entry  
  
# Define a working directory  
WORKDIR /kb-data  
  
# Define the default command as an entrypoint  
ENTRYPOINT ["/usr/local/bin/entry"]  
  
# Expose ports  
# Expose 5601: Kibana default HTTP port  
EXPOSE 5601  

