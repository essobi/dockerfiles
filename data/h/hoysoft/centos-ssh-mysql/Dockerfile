#
=============================================================================  
# jdeathe/centos-ssh-mysql  
#  
# CentOS-6, MySQL 5.1  
#  
#
=============================================================================  
FROM jdeathe/centos-ssh:centos-7-2.1.3  
  
MAINTAINER James Deathe <james.deathe@gmail.com>  
  
#
-----------------------------------------------------------------------------  
# Install MySQL  
#
-----------------------------------------------------------------------------  
RUN rpm --rebuilddb \  
&& yum --setopt=tsflags=nodocs -y install \  
mysql-server-5.1.73-7.el6 \  
&& yum versionlock add \  
mysql* \  
; rm -rf /var/cache/yum/* \  
; yum clean all  
  
#
-----------------------------------------------------------------------------  
# Copy files into place  
#
-----------------------------------------------------------------------------  
ADD usr/sbin/mysqld-bootstrap \  
usr/sbin/mysqld-wrapper \  
/usr/sbin/  
ADD opt/scmi \  
/opt/scmi/  
ADD etc/systemd/system \  
/etc/systemd/system/  
ADD etc/services-config/mysql/my.cnf \  
etc/services-config/mysql/mysqld-bootstrap.conf \  
/etc/services-config/mysql/  
ADD etc/services-config/supervisor/supervisord.d \  
/etc/services-config/supervisor/supervisord.d/  
  
RUN ln -sf \  
/etc/services-config/mysql/my.cnf \  
/etc/my.cnf \  
&& ln -sf \  
/etc/services-config/mysql/mysqld-bootstrap.conf \  
/etc/mysqld-bootstrap.conf \  
&& ln -sf \  
/etc/services-config/supervisor/supervisord.d/mysqld-bootstrap.conf \  
/etc/supervisord.d/mysqld-bootstrap.conf \  
&& ln -sf \  
/etc/services-config/supervisor/supervisord.d/mysqld-wrapper.conf \  
/etc/supervisord.d/mysqld-wrapper.conf \  
&& chmod 600 \  
/etc/services-config/mysql/{my.cnf,mysqld-bootstrap.conf} \  
&& chmod 700 \  
/usr/sbin/mysqld-{bootstrap,wrapper}  
  
EXPOSE 3306  
#
-----------------------------------------------------------------------------  
# Set default environment variables  
#
-----------------------------------------------------------------------------  
ENV MYSQL_ROOT_PASSWORD="" \  
MYSQL_ROOT_PASSWORD_HASHED=false \  
MYSQL_SUBNET="127.0.0.1" \  
MYSQL_USER="" \  
MYSQL_USER_DATABASE="" \  
MYSQL_USER_PASSWORD="" \  
MYSQL_USER_PASSWORD_HASHED=false \  
SSH_AUTOSTART_SSHD=false \  
SSH_AUTOSTART_SSHD_BOOTSTRAP=false  
#
-----------------------------------------------------------------------------  
# Set image metadata  
#
-----------------------------------------------------------------------------  
ARG RELEASE_VERSION="1.7.2"  
LABEL \  
install="docker run \  
\--rm \  
\--privileged \  
\--volume /:/media/root \  
jdeathe/centos-ssh-mysql:centos-6-${RELEASE_VERSION} \  
/usr/sbin/scmi install \  
\--chroot=/media/root \  
\--name=\${NAME} \  
\--tag=centos-7-${RELEASE_VERSION} \  
\--setopt='--volume {{NAME}}.data-mysql:/var/lib/mysql'" \  
uninstall="docker run \  
\--rm \  
\--privileged \  
\--volume /:/media/root \  
jdeathe/centos-ssh-mysql:centos-6-${RELEASE_VERSION} \  
/usr/sbin/scmi uninstall \  
\--chroot=/media/root \  
\--name=\${NAME} \  
\--tag=centos-7-${RELEASE_VERSION} \  
\--setopt='--volume {{NAME}}.data-mysql:/var/lib/mysql'" \  
org.deathe.name="centos-ssh-mysql" \  
org.deathe.version="${RELEASE_VERSION}" \  
org.deathe.release="jdeathe/centos-ssh-mysql:centos-6-${RELEASE_VERSION}" \  
org.deathe.license="MIT" \  
org.deathe.vendor="jdeathe" \  
org.deathe.url="https://github.com/jdeathe/centos-ssh-mysql" \  
org.deathe.description="CentOS-7 7.2 x86_64 - MySQL 5.1."  
  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
RUN mkdir -p /home/workdata  
VOLUME /home/workdata  
  
CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisord.conf"]  

