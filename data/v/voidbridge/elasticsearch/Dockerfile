FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
LABEL io.k8s.description="ElasticSearch" \  
io.k8s.display-name="ElasticSearch" \  
io.openshift.expose-services="9200:rest, 9300:transport"  
ADD files/etc/yum.repos.d /etc/yum.repos.d  
RUN yum install -y java-1.8.0-openjdk elasticsearch-2.3.2 bind-utils && \  
yum clean all -y && \  
find /etc/elasticsearch /var/log/elasticsearch /var/lib/elasticsearch -type d
-exec chmod 777 {} + && \  
find /etc/elasticsearch /var/log/elasticsearch /var/lib/elasticsearch -type f
-exec chmod 666 {} +  
RUN /usr/share/elasticsearch/bin/plugin install -b io.fabric8/elasticsearch-
cloud-kubernetes/2.3.2  
  
ADD files /  
RUN chmod 755 /usr/bin/run-elasticsearch  
  
ENV NODE_QUORUM=1 \  
RECOVER_AFTER_NODES=1 \  
RECOVER_EXPECTED_NODES=1 \  
RECOVER_AFTER_TIME=5m \  
LOG_LEVEL=INFO  
  
USER 1001  
EXPOSE 9200 9300  
VOLUME /mnt/data  
CMD ["run-elasticsearch"]  

