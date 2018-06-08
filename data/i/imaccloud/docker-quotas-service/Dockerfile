FROM ubuntu:14.04  
MAINTAINER Kyle.Bai  
  
USER root  
  
# OpenSSH Server and Configuration  
RUN apt-get update && \  
apt-get install -y openssh-server git mysql-client \  
postgresql-client python-MySQLdb \  
mongodb-server mongodb-clients python-pymongo python-pip  
RUN mkdir /var/run/sshd  
RUN echo 'root:openstack' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Python package install  
RUN pip install --upgrade pip && pip install django sqlalchemy  
  
# Copy quotas services packages  
COPY quotas_service /opt/quotas_service  
ENV QUOTAS_HOME /opt/quotas_service  
  
RUN mkdir -p /etc/log/ && \  
mkdir -p /opt/log/web/ && \  
mkdir -p /opt/log/service/ && \  
mkdir -p /var/log/log_service/ && \  
touch /var/log/log_service/background_service && \  
touch touch /var/log/log_service/web_service  
  
RUN cp -R $QUOTAS_HOME/file/setting/setting.py /etc/log/ && \  
cp -R $QUOTAS_HOME/file/web/* /opt/log/web/ && \  
cp -R $QUOTAS_HOME/file/service/* /opt/log/service/ && \  
cp -R $QUOTAS_HOME/file/init.d/log-service /etc/init.d  
  
# Update boot script  
COPY boot_run.sh /etc/boot_run.sh  
RUN chown root.root /etc/boot_run.sh && chmod 700 /etc/boot_run.sh  
  
# Expose services  
EXPOSE 22 8080  
ENTRYPOINT ["/etc/boot_run.sh"]  

