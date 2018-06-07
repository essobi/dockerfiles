FROM java:8  
# you may probably need more than that for inputs  
EXPOSE 80 9350  
ENV GRAYLOG2_ROOT_USERNAME=admin GRAYLOG2_ROOT_PASSWORD=bruteful \  
GRAYLOG2_IS_MASTER=true \  
GRAYLOG2_MONGODB_URI= \  
GRAYLOG2_ELASTICSEARCH_HOSTS= GRAYLOG2_ELASTICSEARCH_CLUSTER_NAME=graylog2 \  
VERSION=1.3.4  
ADD
https://packages.graylog2.org/releases/graylog2-server/graylog-${VERSION}.tgz
\  
/tmp/graylog-server.tgz  
  
# you may use following instruction for direct archive copying instead of  
# downloading it every time  
#COPY graylog-1.2.2.tgz /tmp/graylog-server.tgz  
RUN tar -xzvf /tmp/graylog-server.tgz -C /tmp \  
&& mv /tmp/graylog-${VERSION} /usr/local/graylog \  
&& rm /tmp/graylog-server.tgz  
ADD bin/* /usr/local/graylog/bin/  
ADD configuration/graylog.conf /etc/graylog/server/server.conf  
  
CMD ["/usr/local/graylog/bin/graylog-docker-wrapper.sh"]  
  

