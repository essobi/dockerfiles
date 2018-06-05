# VERSION 1.0  
# AUTHOR: Jerome Guibert <jguibert@gmail.com>  
# DESCRIPTION: ElasticSearch  
# TO_BUILD: docker build --rm -t airdock/elasticsearch .  
# SOURCE: https://github.com/airdock-io/docker-elasticsearch  
# Pull base image.  
FROM airdock/oracle-jdk:1.8  
MAINTAINER Jerome Guibert <jguibert@gmail.com>  
  
# installed version  
ENV ELASTICSEARCH_VERSION 1.4.5  
# Add configuration file  
ADD config/*.yml /tmp/  
  
# add gpg key for elasticsearch  
# install elasticsearch and obz/elasticsearch-head plugin  
RUN apt-get update -qq && apt-get install -y --no-install-recommends ca-
certificates && \  
curl https://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
&& \  
echo 'deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable
main' > /etc/apt/sources.list.d/elasticsearch.list && \  
apt-get update -qq && \  
apt-get install -y elasticsearch=$ELASTICSEARCH_VERSION && \  
rm /etc/elasticsearch/*.yml && \  
mv /tmp/*.yml /etc/elasticsearch && \  
mkdir -p /var/lib/elasticsearch /usr/share/elasticsearch/plugins && \  
chown -R elasticsearch:elasticsearch /var/log/elasticsearch
/var/lib/elasticsearch /usr/share/elasticsearch/plugins && \  
/usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head && \  
/root/post-install  
  
# Mountable data directories.  
VOLUME ["/var/lib/elasticsearch", "/var/log/elasticsearch"]  
  
# Expose HTTP and transport port  
EXPOSE 9200 9300  
# Define default command.  
CMD ["tini", "-g", "--", "gosu", "elasticsearch:elasticsearch",
"/usr/share/elasticsearch/bin/elasticsearch", "--default.config"
,"/etc/elasticsearch/elasticsearch.yml"]  

