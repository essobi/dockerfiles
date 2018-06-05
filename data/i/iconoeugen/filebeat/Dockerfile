FROM centos:7  
MAINTAINER Horatiu Eugen Vlad <info@vlad.eu>  
  
RUN yum install -y epel-release && \  
yum -y install curl nss_wrapper && \  
yum clean all  
  
ENV USER=filebeat \  
HOME=/usr/share/filebeat \  
PATH=/usr/share/filebeat/bin:$PATH  
  
ENV CONF_DIR=/etc/filebeat \  
PROSPECTOR_DIR=/etc/filebeat/conf.d \  
INIT_DIR=/etc/filebeat/init.d \  
DATA_DIR=/var/lib/filebeat \  
LOGS_DIR=/var/log/filebeat  
  
ENV BEATS_VERSION 5.3.0  
RUN yum -y install
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${BEATS_VERSION}-x86_64.rpm
&& \  
yum clean all  
COPY passwd.in ${HOME}/  
COPY entrypoint /  
COPY filebeat.yml ${CONF_DIR}/filebeat.yml  
  
RUN useradd -d ${HOME} -g root -m -N -s /sbin/nologin ${USER} && \  
for path in ${HOME} ${CONF_DIR} ${DATA_DIR} ${LOGS_DIR} ${INIT_DIR}
${CONF_DIR}/conf.d; do \  
mkdir -p "$path" && chmod -R ug+rwX,o-rwx "$path" && chown -R root:root
"$path"; \  
done  
  
USER 1000  
WORKDIR /etc/filebeat  
ENTRYPOINT ["/entrypoint"]  
CMD ["filebeat"]  

