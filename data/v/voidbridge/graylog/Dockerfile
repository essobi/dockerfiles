FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
LABEL io.k8s.description="Graylog" \  
io.k8s.display-name="Graylog" \  
io.openshift.expose-services="9000:web, 12900:rest"  
  
RUN rpm -ivh
https://packages.graylog2.org/repo/packages/graylog-2.0-repository_latest.rpm
&& \  
rpm -ivh https://github.com/Graylog2/graylog-plugin-
beats/releases/download/1.0.3/graylog-plugin-beats-1.0.3-1.noarch.rpm && \  
yum install -y --enablerepo=centosplus gettext epel-release && \  
yum install -y java-1.8.0-openjdk graylog-server bind-utils python-pip && \  
pip install j2cli && \  
yum clean all -y && \  
find /etc/graylog /var/lib/graylog-server /var/log/graylog-server -type d
-exec chmod 777 {} + && \  
find /etc/graylog /var/lib/graylog-server /var/log/graylog-server -type f
-exec chmod 666 {} +  
  
ADD files /  
ADD templates /tmp/templates  
RUN chmod 755 /usr/bin/run-graylog  
  
ENV IS_MASTER=true \  
ES_SHARDS=1 \  
ES_REPLICAS=0 \  
LOG_LEVEL_ROOT=warn \  
LOG_LEVEL_GRAYLOG=info  
  
USER 1001  
EXPOSE 9000 12900  
VOLUME /mnt/data  
CMD ["run-graylog"]  

