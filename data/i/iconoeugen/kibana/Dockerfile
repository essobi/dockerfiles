FROM centos:7  
MAINTAINER Horatiu Eugen Vlad <info@vlad.eu>  
  
RUN yum install -y epel-release && \  
yum -y install curl nss_wrapper && \  
yum clean all  
  
ENV USER=kibana \  
HOME=/usr/share/kibana \  
PATH=/usr/share/kibana/bin:$PATH  
  
ENV CONF_DIR=/etc/kibana \  
INIT_DIR=/etc/kibana/init.d \  
DATA_DIR=/var/lib/kibana \  
LOGS_DIR=/var/log/kibana \  
PID_DIR=/var/run  
ENV KIBANA_VERSION 5.3.0-1  
COPY kibana.repo /etc/yum.repos.d/kibana.repo  
RUN yum -y install kibana-${KIBANA_VERSION}.x86_64 && \  
yum clean all  
  
COPY passwd.in ${HOME}/  
COPY entrypoint /  
  
COPY init.d ${INIT_DIR}  
COPY kibana.yml.in ${CONF_DIR}/kibana.yml.in  
  
RUN for path in ${HOME} ${CONF_DIR} ${DATA_DIR} ${LOGS_DIR} ${INIT_DIR}
${PID_DIR} ${CONF_DIR}/conf.d; do \  
mkdir -p "$path" && chmod -R ug+rwX,o-rwx "$path" && chown -R root:root
"$path"; \  
done  
  
EXPOSE 5601  
USER 1000  
WORKDIR /etc/kibana  
ENTRYPOINT ["/entrypoint"]  
CMD ["kibana"]  

