FROM centos:centos6  
  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
# Update base images.  
RUN yum distribution-synchronization -y  
  
# Setup elasticsearch + kibana3  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk.x86_64  
ENV PATH $JAVA_HOME/bin:$PATH  
  
RUN rpm --import https://packages.elasticsearch.org/GPG-KEY-elasticsearch  
ADD ./elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo  
RUN yum install -y elasticsearch java-1.7.0-openjdk-devel cronie  
WORKDIR usr/share/elasticsearch/  
RUN bin/plugin -url http://download.elasticsearch.org/kibana/kibana/kibana-
latest.zip -install elasticsearch/kibana3  
RUN echo 'http.cors.enabled: true' >> /etc/elasticsearch/elasticsearch.yml &&\  
echo 'http.cors.allow-origin: "/.*/"' >> /etc/elasticsearch/elasticsearch.yml  
  
# Setup supervisord  
RUN yum install -y python-setuptools  
RUN easy_install supervisor  
  
# configuration supervisord  
ADD ./supervisord/supervisord.conf /etc/supervisord.conf  
ADD ./run.sh /run.sh  
RUN chmod 755 /run.sh  
  
# Expose the Ports used by  
EXPOSE 9200  
CMD ["/bin/bash", "/run.sh"]  

