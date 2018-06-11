FROM voidbridge/java:latest  
MAINTAINER Tom Dearman <tom.dearman@voidbridge.com>  
  
ARG ZOOKEEPER_VERSION=3.4.8  
RUN yum install -y --enablerepo=centosplus gettext epel-release && \  
yum install -y hostname bind-utils python-pip && \  
pip install j2cli && \  
yum clean all -y  
  
RUN mkdir -p /opt/zookeeper && \  
curl -fL
http://archive.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
| \  
tar -zxf - -C /opt/zookeeper --strip-components 1  
  
ADD files /  
ADD templates /tmp/templates  
RUN chmod 755 /usr/bin/run-zookeeper  
  
ENV HEAP_FRACTION=0.5  
USER 1001  
EXPOSE 2181 2888 3888  
VOLUME /mnt/data  
CMD ["run-zookeeper"]  

