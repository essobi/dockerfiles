FROM centos:centos7  
#MAINTAINER Ushio Shugo <ushio.s@gmail.com>  
# using epel  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
Run yum -y update; yum clean all  
  
# add composer lock file (prevent github timeouts)  
ADD ./root/composer.lock /.composer/composer.lock  
  
ADD ./root/packages.sh /packages.sh  
RUN chmod 755 /packages.sh  
RUN /packages.sh  
  
# set time to EST5EDT  
RUN ln -sf /usr/share/zoneinfo/EST5EDT /etc/localtime  
  
# install postfix  
ADD ./root/packages_postfix.sh /packages_postfix.sh  
RUN chmod 755 /packages_postfix.sh  
RUN /packages_postfix.sh  
  
# postfix config  
ADD ./root/etc/postfix/main.cf /etc/postfix/main.cf  
ADD ./root/etc/postfix/header_checks /etc/postfix/header_checks  
  
# install php71  
ADD ./root/packages_php7.sh /packages_php7.sh  
RUN chmod 755 /packages_php7.sh  
RUN /packages_php7.sh  
  
# install mysql to handle drush issues  
RUN yum -y install mysql && yum clean all  
  
# install nodejs packages  
# 2017-08-16 - TMP removed due to package issue:
https://bugzilla.redhat.com/show_bug.cgi?id=1481470  
ADD ./root/packages_nodejs.sh /nodejs.sh  
RUN chmod 755 /nodejs.sh  
RUN yum-config-manager --enable cr; /nodejs.sh; yum-config-manager --disable
cr  
  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
  
# Add Configs  
ADD ./root/etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf  
ADD ./root/etc/php.ini /etc/php.ini  
ADD ./root/etc/httpd/robots.txt /etc/httpd/robots.txt  
  
# set default umask to 002  
ADD ./root/etc/profile /etc/profile  
ADD ./root/docker-umask-wrapper.sh /bin/docker-umask-wrapper.sh  
  
RUN chmod u+x /bin/docker-umask-wrapper.sh  
  
RUN chmod 755 /*.sh  
RUN mkdir -p /var/lib/php/session  
RUN chmod 777 /var/lib/php/session  
  
# Add php user  
RUN usermod -g users apache  
  
# Ensure composer is in our path  
ENV COMPOSER_HOME /  
ENV PATH /.composer/vendor/bin:$PATH  
  
EXPOSE 80  
CMD postconf -e "test = test"; postconf -e "smtp_sasl_password_maps =
static:$POSTFIX_USER:$POSTFIX_PWD"; postconf -e "myhostname =
$POSTFIX_HOSTNAME"; postfix start; echo -e
"\nxdebug.remote_host=$XDEBUG_CLIENT_IP" >> /etc/php.ini; /bin/docker-umask-
wrapper.sh /usr/sbin/httpd -DFOREGROUND  

