FROM centos:centos7  
MAINTAINER Marcin Ryzycki marcin@m12.io, Przemyslaw Ozgo linux@ozgo.info  
  
ENV KIBANA_VERSION 4.4.1  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y tar java-1.8.0-openjdk && \  
yum clean all && \  
mkdir -p /opt/kibana && \  
cd /opt/kibana && \  
curl -o /tmp/kibana4.tgz
https://download.elastic.co/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
&& \  
tar zxvf /tmp/kibana4.tgz -C /opt/kibana --strip-components=1 && \  
rm -f /tmp/kibana4.tgz  
  
ENV KIBANA_CONFIG=/opt/kibana/config/kibana.yml \  
MARVEL_SUPPORT=false  
  
COPY container-files /  
  
EXPOSE 5601  
ENTRYPOINT ["/bootstrap.sh"]  

