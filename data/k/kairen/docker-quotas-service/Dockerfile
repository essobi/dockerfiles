FROM ubuntu:14.04  
MAINTAINER Kyle.Bai  
  
USER root  
  
# Update and Upgrade  
#RUN apt-get update -y  
#RUN apt-get upgrade -y  
# OpenSSH Server and Configuration  
RUN apt-get update && apt-get install -y openssh-server git  
RUN mkdir /var/run/sshd  
RUN echo 'root:openstack' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# MySQL,MongoDB Install and Configuration  
RUN apt-get install -y mysql-client postgresql-client python-MySQLdb  
  
# ADD my.cnf /etc/mysql/conf.d/my.cnf  
# ADD mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
# ENV MYSQL_USER=mysql \  
# MYSQL_DATA_DIR=/var/lib/mysql \  
# MYSQL_RUN_DIR=/run/mysqld \  
# MYSQL_LOG_DIR=/var/log/mysql  
# ENV DEBIAN_FRONTEND noninteractive  
# RUN apt-get update && \  
# apt-get -yq install mysql-server-5.5 pwgen && \  
# rm -rf /var/lib/apt/lists/* && \  
# rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf && \  
# if [ ! -f /usr/share/mysql/my-default.cnf ] ; then cp /etc/mysql/my.cnf
/usr/share/mysql/my-default.cnf; fi && \  
# mysql_install_db > /dev/null 2>&1 && \  
# touch /var/lib/mysql/.EMPTY_DB  
# Install MongoDB  
RUN apt-get install -y mongodb-server mongodb-clients python-pymongo  
  
# Python package install  
RUN apt-get install -y python-pip python-dev build-essential  
RUN pip install --upgrade pip  
RUN pip install django sqlalchemy  
  
# Copy quotas services packages  
COPY quotas_service /opt/quotas_service  
ENV QUOTAS_HOME /opt/quotas_service  
RUN mkdir -p /etc/log/  
RUN mkdir -p /opt/log/web/  
RUN mkdir -p /opt/log/service/  
RUN mkdir -p /var/log/log_service/  
RUN touch /var/log/log_service/background_service  
RUN touch /var/log/log_service/web_service  
RUN cp -R $QUOTAS_HOME/file/setting/setting.py /etc/log/  
RUN cp -R $QUOTAS_HOME/file/web/* /opt/log/web/  
RUN cp -R $QUOTAS_HOME/file/service/* /opt/log/service/  
RUN cp -R $QUOTAS_HOME/file/init.d/log-service /etc/init.d  
  
# Update boot script  
COPY boot_run.sh /etc/boot_run.sh  
RUN chown root.root /etc/boot_run.sh  
RUN chmod 700 /etc/boot_run.sh  
  
# Expose services  
EXPOSE 22  
EXPOSE 8080  
ENTRYPOINT ["/etc/boot_run.sh"]

