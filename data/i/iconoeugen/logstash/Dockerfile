FROM centos:7  
MAINTAINER Horatiu Eugen Vlad <info@vlad.eu>  
  
RUN yum install -y epel-release && \  
yum -y install curl nss_wrapper java-1.8.0-openjdk.x86_64 && \  
yum clean all  
  
ENV USER=logstash \  
HOME=/usr/share/logstash \  
PATH=/usr/share/logstash/bin:$PATH \  
JAVACMD=/usr/bin/java  
  
ENV LS_SETTINGS_DIR=/etc/logstash \  
LS_INIT_DIR=/etc/logstash/init.d \  
LS_CONF_DIR=/etc/logstash/conf.d \  
LS_DATA_DIR=/var/lib/logstash \  
LS_LOGS_DIR=/var/log/logstash  
  
COPY logstash.repo /etc/yum.repos.d/logstash.repo  
ENV LS_VERSION 1:5.3.0-1  
RUN yum -y install logstash-${LS_VERSION}.noarch && \  
yum clean all  
  
COPY passwd.in ${HOME}/  
COPY entrypoint /  
  
RUN for path in ${HOME} ${LS_SETTINGS_DIR} ${LS_CONF_DIR} ${LS_INIT_DIR}
${LS_DATA_DIR} ${LS_LOGS_DIR}; do \  
mkdir -p "$path" && chmod -R ug+rwX "$path" && chown -R $USER:root "$path"; \  
done  
USER 1000  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["logstash"]  

