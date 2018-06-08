FROM java:8  
MAINTAINER Dejan Lukan <dejan@proteansec.com>  
  
WORKDIR /opt  
ENV elasticsearchurl
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.6.0.tar.gz  
ENV kibanaurl
https://download.elastic.co/kibana/kibana/kibana-4.1.1-linux-x64.tar.gz  
ENV logstashurl
https://download.elastic.co/logstash/logstash/logstash-1.5.2.tar.gz  
  
# Add sudo: http://stackoverflow.com/questions/25845538/using-sudo-inside-a-
docker-container  
RUN apt-get update  
RUN apt-get -y install wget supervisor sudo ssh  
RUN apt-get -y install net-tools vim netcat  
RUN useradd docker && echo "docker:docker" | chpasswd && adduser docker sudo  
RUN mkdir -p /home/docker && chown -R docker:docker /home/docker  
  
# SSH requires this direcotry for privilege separation.  
RUN mkdir -p /var/run/sshd  
  
# Install Elasticsearch  
RUN \  
sudo wget --quiet --directory-prefix . ${elasticsearchurl} && \  
sudo mkdir -p "elasticsearch" && \  
sudo tar xzf elasticsearch-*.tar.gz -C "elasticsearch" \--strip-components=1
&& \  
sudo rm /opt/elasticsearch-*.tar.gz && \  
echo "network.host: localhost" >> elasticsearch/config/elasticsearch.yml  
  
# Install Kibana  
RUN \  
sudo wget --quiet --directory-prefix . ${kibanaurl} && \  
sudo mkdir -p "kibana" && \  
sudo tar xzf kibana-*.tar.gz -C "kibana" \--strip-components=1 && \  
sudo rm /opt/kibana-*.tar.gz && \  
sudo sed -i "s/host: \"0.0.0.0\"/host: \"127.0.0.1\"/g"
kibana/config/kibana.yml  
  
# Install Logstash  
RUN \  
sudo wget --quiet --directory-prefix . ${logstashurl} && \  
sudo mkdir -p "logstash/" && \  
sudo tar xzf logstash-*.tar.gz -C "logstash" \--strip-components=1 && \  
sudo rm /opt/logstash-*.tar.gz && \  
sudo mkdir -p "logstash/conf.d/"  
ADD logstash/10-syslog.conf logstash/conf.d/10-syslog.conf  
  
# Supervisor  
RUN sudo mkdir -p "/etc/supervisor/conf.d/"  
ADD supervisor/default.conf /etc/supervisor/conf.d/  
ADD supervisor/elasticsearch.conf /etc/supervisor/conf.d/  
ADD supervisor/kibana.conf /etc/supervisor/conf.d/  
ADD supervisor/logstash.conf /etc/supervisor/conf.d/  
ADD supervisor/sshd.conf /etc/supervisor/conf.d/  
CMD ["/usr/bin/supervisord", "-n"]  

