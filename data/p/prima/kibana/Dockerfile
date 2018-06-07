FROM docker.elastic.co/kibana/kibana:6.2.3  
  
USER root  
  
RUN yum -y update && \  
yum -y install python wget && \  
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \  
python get-pip.py && \  
rm get-pip.py && \  
pip install awscli \--upgrade && \  
curl -L -o ./biscuit-linux_amd64.tgz
https://github.com/dcoker/biscuit/releases/download/v0.1.3/biscuit-
linux_amd64.tgz && \  
tar xzvf biscuit-linux_amd64.tgz && \  
mv biscuit /usr/bin/biscuit && \  
chmod +x /usr/bin/biscuit && \  
rm biscuit-linux_amd64.tgz && \  
rm -rf /var/cache/yum && \  
yum clean all && \  
curl -L -o ./search-guard-kibana-plugin.zip
https://search.maven.org/remotecontent?filepath=com/floragunn/search-guard-
kibana-plugin/6.2.3-12/search-guard-kibana-plugin-6.2.3-12.zip && \  
./bin/kibana-plugin install file://$PWD/search-guard-kibana-plugin.zip && \  
rm -f search-guard-kibana-plugin.zip && \  
chown kibana:kibana $PWD -R  
  
USER kibana  
# TZ: https://github.com/primait/board/issues/1631  
ENV ELASTICSEARCH_URL=http://es-searches-production.prima.prod:9200 \  
XPACK_SECURITY_ENABLED=false \  
XPACK_MONITORING_ENABLED=true \  
XPACK_MONITORING_KIBANA_COLLECTION_ENABLED=true \  
XPACK_MONITORING_UI_CONTAINER_ELASTICSEARCH_ENABLED=false \  
ELASTICSEARCH_REQUESTTIMEOUT=300000 \  
TZ=:/etc/localtime  
  
COPY ./files/entrypoint.sh /entrypoint.sh  
  
RUN /usr/local/bin/kibana-docker 2>&1 | grep -m 1 "Optimization of .* complete
in .* seconds"  
ENTRYPOINT ["/entrypoint.sh"]  

