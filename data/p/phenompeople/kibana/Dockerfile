FROM centos:7.4.1708  
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com" \  
version="6.1.2" \  
project="kibana"  
EXPOSE 5601  
ARG KIBANA_VERSION=6.1.2  
ENV container docker \  
PACKAGE_VERSION=${KIBANA_VERSION}  
ARG APP_HOME=/usr/local/kibana  
RUN yum install -y -q wget && \  
groupadd -g 405 kibana && \  
useradd -u 405 -g 405 kibana && \  
wget -q -O /tmp/kibana.tar.gz
https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz
&& \  
tar -xzf /tmp/kibana.tar.gz -C /usr/local && \  
ln -sf /usr/local/kibana-${KIBANA_VERSION}-linux-x86_64 ${APP_HOME} && \  
mkdir -p /var/log/kibana /etc/kibana && \  
rm -rf /tmp/kibana.tar.gz && \  
touch /var/log/kibana/kibana.log  
COPY setup/config/kibana.yml /etc/kibana/kibana.yml  
ADD setup/scripts /usr/local/kibana/  
RUN chown -R kibana:kibana /usr/local/kibana-${KIBANA_VERSION}-linux-x86_64
/var/log/kibana /etc/kibana && \  
/usr/local/kibana/bin/kibana-plugin install
https://github.com/sivasamyk/logtrail/releases/download/v0.1.25/logtrail-6.1.2-0.1.25.zip  
COPY setup/config/logtrail.json
/usr/local/kibana/plugins/logtrail/logtrail.json  
ENTRYPOINT ["/usr/local/kibana/kibana.sh"]  

