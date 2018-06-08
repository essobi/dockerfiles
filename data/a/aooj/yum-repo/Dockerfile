FROM centos:7.4.1708  
MAINTAINER AooJ <aooj@n13.cz>  
  
# ENV FAKE_SYSTEMCTL=https://raw.githubusercontent.com/gdraheim/docker-
systemctl-
replacement/b9b2c8ecf8a5d2b986060fc1592055e75b84a6b8/files/docker/systemctl.py  
# RUN curl -o /usr/bin/systemctl ${FAKE_SYSTEMCTL} && \  
# chmod 0755 /usr/bin/systemctl  
ARG CDH_VERSION=5.14.1  
ENV CDH_VERSION=$CDH_VERSION  
ENV GPG_KEY=https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/RPM-GPG-KEY-
cloudera  
  
RUN echo -e "[cloudera-manager] \n\  
name = cloudera-manager \n\  
description = Cloudera Manager repository \n\  
baseurl = https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/${CDH_VERSION}/
\n\  
gpgkey=${GPG_KEY} \n\  
gpgcheck=1 \n\  
enabled=1 \n\  
" > /etc/yum.repos.d/cloudera-manager.repo  
  
RUN yum install -y reposync createrepo httpd && \  
rpm --import ${GPG_KEY} && \  
reposync --gpgcheck --download-metadata -p /var/www/html -r cloudera-manager
-l && \  
createrepo /var/www/html && \  
curl -o /var/www/html/RPM-GPG-KEY-cloudera ${GPG_KEY} && \  
echo > /etc/httpd/conf.d/welcome.conf && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
VOLUME ["/var/www/html"]  
  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-DFOREGROUND"]

