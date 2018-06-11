FROM centos  
  
MAINTAINER wenjianzhou <nihao-wenjian@163.com>  
  
# basic settings  
ENV TZ=Asia/Shanghai \  
LANG=en_US.UTF-8 \  
PW=root  
  
RUN set -x \  
&& ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \  
&& echo "root:${PW}" | chpasswd  
  
# basic paths  
ENV TOP_HOME=/root  
ENV APP_HOME=${TOP_HOME}/app \  
BIN_PATH=${TOP_HOME}/bin PATH=${PATH}:${TOP_HOME}/bin \  
USR_PATH=${TOP_HOME}/usr \  
WWW_ROOT=${TOP_HOME}/www  
  
RUN chmod a+x root && mkdir -p ${APP_HOME} ${BIN_PATH} ${USR_PATH} ${WWW_ROOT}
&& rm -f /root/anaconda-ks.cfg  
  
# basic tools  
RUN set -x \  
&& yum -y install wget unzip net-tools sysstat lrzsz \  
&& yum clean all  
  
# jdk  
ENV JAVA_DOWNLOAD_URL="http://download.oracle.com/otn-
pub/java/jdk/8u172-b11/a58eab1ec242421181065cdc37240b08/jdk-8u172-linux-x64.rpm"
\  
JAVA_HOME=/usr/java/latest  
  
RUN set -x \  
&& wget -q --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" ${JAVA_DOWNLOAD_URL} -O
/tmp/java.rpm \  
&& yum -y install /tmp/java.rpm \  
&& yum clean all && rm -rf /tmp/*  
  
# filebeat  
ENV
FILEBEAT_DOWNLOAD_URL="https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.1.1-linux-x86_64.tar.gz"
\  
FILEBEAT_HOME=${USR_PATH}/filebeat-5.1.1-linux-x86_64  
  
RUN wget -q ${FILEBEAT_DOWNLOAD_URL} -O /tmp/filebeat.tar.gz \  
&& tar -xzf /tmp/filebeat.tar.gz -C ${USR_PATH} \  
&& rm -rf /tmp/*  
  
# glassfish  
ENV
GLASSFISH_DOWNLOAD_URL="http://download.oracle.com/glassfish/4.1.1/release/glassfish-4.1.1.zip"
\  
GLASSFISH_HOME=${USR_PATH}/glassfish4 \  
GLASSFISH_DOMAIN=${USR_PATH}/glassfish4/glassfish/domains/domain1 \  
PATH=${PATH}:${USR_PATH}/glassfish4/bin  
  
RUN set -x \  
&& wget -q ${GLASSFISH_DOWNLOAD_URL} -O /tmp/glassfish.zip \  
&& unzip -o /tmp/glassfish.zip -d ${USR_PATH} \  
&& rm -rf ${GLASSFISH_DOMAIN}/logs && ln -sf /var/log ${GLASSFISH_DOMAIN}/logs
\  
&& rm -rf /tmp/*  
  
# nginx  
ENV NGINX_DOWNLOAD_URL="http://nginx.org/packages/centos/7/noarch/RPMS/nginx-
release-centos-7-0.el7.ngx.noarch.rpm" \  
NGINX_CONF_PATH=/etc/nginx/conf.d  
  
RUN set -x \  
&& wget -q ${NGINX_DOWNLOAD_URL} -O /tmp/nginx.rpm \  
&& yum -y install /tmp/nginx.rpm \  
&& yum -y install nginx \  
&& rm -rf ${NGINX_CONF_PATH}/* \  
&& rm -rf /tmp/*  
  
# sshd  
RUN set -x \  
&& yum install -y openssh-server openssh-clients \  
&& ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \  
&& ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key \  
&& ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key \  
&& yum clean all  
  
EXPOSE 22  
# add files  
COPY files/bin/* ${BIN_PATH}/  
COPY files/filebeat/* ${FILEBEAT_HOME}/  
COPY files/glassfish/* ${GLASSFISH_DOMAIN}/config/  
COPY files/nginx/* ${NGINX_CONF_PATH}/  
COPY files/ssh/authorized_keys /root/.ssh/  
  
EXPOSE 4848 8080 8181  
CMD ["/usr/sbin/sshd", "-D"]

