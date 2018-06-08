FROM pblittle/base:0.3.0  
MAINTAINER Rex Posadas <rexposadas@yahoo.com>  
  
# Download latest package lists  
RUN apt-get update  
  
# Install dependencies  
RUN apt-get install -yq \  
openjdk-7-jre-headless \  
wget  
  
# Download version 1.4.2 of logstash  
RUN cd /tmp && \  
wget
https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz &&
\  
tar -xzvf ./logstash-1.4.2.tar.gz && \  
mv ./logstash-1.4.2 /opt/logstash && \  
rm ./logstash-1.4.2.tar.gz  
  
# Copy build files to container root  
RUN mkdir /app  
ADD . /app  
  
# Elasticsearch  
EXPOSE 9200  
# Kibana  
EXPOSE 9292  
# Syslog  
EXPOSE 514  
# TCP  
EXPOSE 7000  
# Start logstash  
CMD /app/bin/boot  
# CMD /opt/logstash/bin/logstash -e 'input {tcp {port => 7000}} output
{elasticsearch {host => "127.0.0.1"}}'  

