FROM centos:7.2.1511  
LABEL MAINTAINER="Hortonworks"  
  
RUN yum install -y git bind-utils unzip wget which java-1.8.0-openjdk cronie \  
http://s3.amazonaws.com/dev.hortonworks.com/hst/centos7/smartsense-
hst-1.4.1.2.5.0.1-1817.x86_64.rpm \  
&& yum clean all \  
&& rm -fr /var/tmp/yum*  
  
RUN curl -Lo /usr/bin/jq http://stedolan.github.io/jq/download/linux64/jq &&
chmod +x /usr/bin/jq  
  
WORKDIR /var/lib/cloudbreak-deployment  
  
ADD etc/yum.repos.d/ambari.repo /etc/yum.repos.d/ambari.repo  
ADD bootstrap/hst-capture.sh /var/lib/smartsense/hst-capture.sh  
ADD bootstrap/topology.json /var/lib/smartsense/hst-agent/data/topology.json  
  
ADD bootstrap/export/cp_cfg.sh /var/lib/smartsense/hst-
agent/resources/collection-scripts/cloudbreak/scripts/cp_cfg.sh  
ADD bootstrap/export/cp_log.sh /var/lib/smartsense/hst-
agent/resources/collection-scripts/cloudbreak/scripts/cp_log.sh  
ADD bootstrap/export/cp_etc.sh /var/lib/smartsense/hst-
agent/resources/collection-scripts/cloudbreak/scripts/cp_etc.sh  
ADD bootstrap/cloudbreak-capture-specification.xml /var/lib/smartsense/hst-
agent/resources/collection-scripts/cloudbreak/cloudbreak-capture-
specification.xml  
  
ADD bootstrap/cloudbreak-flex-usage.sh /var/lib/smartsense/hst-
agent/resources/collection-scripts/cloudbreak/scripts/cloudbreak-flex-usage.sh  
  
ADD bootstrap/export/anonymization.ini /etc/hst/conf/anonymization.ini  
ADD bootstrap/export/anonymization_rules.json
/etc/hst/conf/anonymization_rules.json  
  
ADD bootstrap/start-hst.sh /var/lib/smartsense/start-hst.sh  
  
ENTRYPOINT ["/var/lib/smartsense/start-hst.sh"]

