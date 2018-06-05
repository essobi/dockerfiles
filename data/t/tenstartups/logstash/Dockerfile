#  
# Extension to the base Logstash docker image with additional input/output
plugins.  
#  
# http://github.com/tenstartups/logstash-docker  
#  
FROM docker.elastic.co/logstash/logstash:5.6.3  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
USER root  
  
# Install packages.  
RUN \  
yum install -y ruby git  
  
# Install additional logstash plugins.  
RUN \  
cd /tmp && \  
git clone https://github.com/logstash-plugins/logstash-input-journald.git && \  
cd logstash-input-journald && \  
gem build logstash-input-journald.gemspec && \  
logstash-plugin install ./logstash-input-journald-*.gem  
  
# Copy files into place.  
COPY entrypoint.sh /docker-entrypoint.sh  

