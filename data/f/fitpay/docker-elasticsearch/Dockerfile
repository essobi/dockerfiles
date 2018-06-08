FROM centos  
  
RUN yum update -y; yum clean all  
RUN yum install -y java-1.7.0-openjdk-headless wget tar rsyslog; yum clean all  
  
RUN cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-2.2.0.tar.gz
&& \  
tar xvzf elasticsearch-2.2.0.tar.gz && \  
rm -f elasticsearch-2.2.0.tar.gz && \  
mv /tmp/elasticsearch-2.2.0 /elasticsearch  
  
RUN /elasticsearch/bin/plugin install cloud-aws  
RUN /elasticsearch/bin/plugin install lmenezes/elasticsearch-kopf/2.x  
  
VOLUME ["/data"]  
  
ADD elasticsearch.yml /elasticsearch-default.yml  
  
WORKDIR /data  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

