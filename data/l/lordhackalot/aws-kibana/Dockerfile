FROM centos:centos6  
MAINTAINER nattapon <lordhackalot@gmail.com>  
ENV KIBANA_CONFIG /opt/kibana/config/kibana.yml  
ENV fileshared 52.74.40.153  
RUN rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y tar java-1.7.0-openjdk && \  
mkdir -p /opt/kibana && cd /opt/kibana && \  
curl -o /tmp/kibana4.tgz
http://${fileshared}/kibana/kibana-4.0.2-linux-x64.tar.gz && \  
tar zxvf /tmp/kibana4.tgz -C /opt/kibana --strip-components=1 && \  
rm -f /tmp/kibana4.tgz  
RUN curl -o /bootstrap.sh -SL http://${fileshared}/kibana/bootstrap.sh  
RUN curl -o /opt/kibana/config/kibana.yml -SL
http://${fileshared}/kibana/kibana.yml  
#COPY bootstrap.sh /  
EXPOSE 5601  
ENTRYPOINT ["/bin/bash","/bootstrap.sh"]  

