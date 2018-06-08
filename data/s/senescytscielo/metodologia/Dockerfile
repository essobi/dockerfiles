FROM centos:6.8  
MAINTAINER Infrastructure SciELO <infra@scielo.org>  
  
ENV INSTANCE_NAME scielo_br  
ENV USER_SUPERVISOR root  
ENV PASS_SUPERVISOR toor  
ENV SITE_NAME www.scielo.br  
ENV USER_FTP user_ftp  
ENV PASSWD_FTP passwd_ftp  
ENV USER_PASS scielo123  
ENV GID 1000  
ENV GIT_BRANCH_NAME scielo_scl  
  
# Resolving dependencies from php 5.2.17.  
RUN yum -y update && \  
yum -y install aspell-devel.x86_64 && yum clean all && \  
yum -y install wget.x86_64 && yum clean all && \  
yum -y install libxslt-devel.x86_64 && \  
yum -y install openssh-server.x86_64 openssh-clients ftp rsync zip unzip&& \  
yum clean all  
  
RUN yum install -y openssl098e-0.9.8e-20.el6.centos.1 && \  
yum install -y httpd.x86_64 httpd-devel autoconf automake && \  
yum install -y freetype libjpeg-turbo-1.2.1-3.el6_5 libpng-1.2.49-2.el6_7
libxslt-1.1.26-2.el6_3.1 && \  
yum clean all  
  
COPY php-5.2.17-centos5.5-64bits/* /php-5.2.17-centos5.5-64bits/  
  
#Install php packages version 5.2.17 and their dependencies.  
RUN rpm -hiv /php-5.2.17-centos5.5-64bits/mhash-0.9.9.9-3.el6.x86_64.rpm && \  
rpm -hiv /php-5.2.17-centos5.5-64bits/libmcrypt-2.5.8-9.el6.x86_64.rpm && \  
rpm -hiv /php-5.2.17-centos5.5-64bits/compat-
libcurl3-7.15.5-2.el5.remi.x86_64.rpm && \  
rpm -hiv /php-5.2.17-centos5.5-64bits/php-cli-5.2.17-1.x86_64.rpm
/php-5.2.17-centos5.5-64bits/php-common-5.2.17-1.x86_64.rpm && \  
rpm -hiv /php-5.2.17-centos5.5-64bits/php-bcmath-5.2.17-1.x86_64.rpm
/php-5.2.17-centos5.5-64bits/php-5.2.17-1.x86_64.rpm \  
/php-5.2.17-centos5.5-64bits/php-devel-5.2.17-1.x86_64.rpm \  
/php-5.2.17-centos5.5-64bits/php-gd-5.2.17-1.x86_64.rpm
/php-5.2.17-centos5.5-64bits/php-mbstring-5.2.17-1.x86_64.rpm \  
/php-5.2.17-centos5.5-64bits/php-mcrypt-5.2.17-1.x86_64.rpm \  
/php-5.2.17-centos5.5-64bits/php-mhash-5.2.17-1.x86_64.rpm
/php-5.2.17-centos5.5-64bits/php-pdo-5.2.17-1.x86_64.rpm \  
/php-5.2.17-centos5.5-64bits/php-soap-5.2.17-1.x86_64.rpm
/php-5.2.17-centos5.5-64bits/php-xml-5.2.17-1.x86_64.rpm
/php-5.2.17-centos5.5-64bits/php-xmlrpc-5.2.17-1.x86_64.rpm  
  
#Install supervisord  
RUN \  
yum install -y epel-release && \  
yum install -y iproute python-setuptools hostname inotify-tools yum-utils
which && \  
yum clean all && \  
easy_install supervisor  
  
# Creating sshd pid directory  
RUN mkdir -p /var/run/sshd  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Clean php packages to reduce image size.  
RUN rm -Rf /php-5.2.17-centos5.5-64bits/  
  
# Directory where application web and log will be save.  
VOLUME /var/www/scielo  
VOLUME /var/www/apache  
  
# Create directory where virtual host will be save. Create directory scripts
and supervisor log  
RUN mkdir /etc/httpd/conf.d/vhosts \  
&& mkdir /scripts \  
&& mkdir /var/log/supervisor  
  
# Remove original httpd.conf file to accept new one.  
RUN rm -f /etc/httpd/conf/httpd.conf  
  
# copy http files  
COPY conf/httpd.conf.template /etc/httpd/conf/httpd.conf  
COPY conf/vhosts.conf.template /etc/httpd/conf.d/vhosts/vhosts.conf  
COPY conf/virtual_host.conf.template
/etc/httpd/conf.d/vhosts/virtual_host.conf  
COPY scripts/compacta_log.sh.template /scripts/compacta_log.sh  
COPY conf/supervisord.conf.template /etc/supervisord.conf  
  
## Suppress error message 'Could not load host key: ...'  
RUN /usr/bin/ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -C '' -N ''  
RUN /usr/bin/ssh-keygen -t rsa -f /etc/ssh/ssh_host_dsa_key -C '' -N ''  
  
##Creating user and group do execute the container  
RUN groupadd -f -g $GID scielo && \  
useradd -c "SciELO User" -u $GID -g scielo scielo && \  
echo "scielo:$USER_PASS" | chpasswd  
  
RUN chown -R scielo.scielo /var/log/supervisor && \  
touch /var/run/supervisord.pid && \  
chown scielo.scielo /var/run/supervisord.pid && \  
chown scielo.scielo -R /etc/httpd && \  
chown scielo.scielo -R /var/log/httpd && \  
chown scielo.scielo -R /var/run/httpd && \  
chown scielo.scielo -R /scripts && \  
chown scielo.scielo /etc/supervisord.conf && \  
chown scielo.scielo /var/run/sshd && \  
chown scielo.scielo /etc/pam.d/sshd && \  
chown scielo.scielo -R /etc/ssh && \  
chown scielo.scielo -R /var/lib/php  
  
EXPOSE 80  
EXPOSE 22  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
USER scielo  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

