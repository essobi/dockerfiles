### Dockerfile  
#  
# See https://github.com/reconnix/docker  
FROM reconnix/base:CentOS6  
MAINTAINER Russ McKendrick <russ.mckendrick@reconnix.com>  
ADD repo-nginx.repo /etc/yum.repos.d/nginx-release.repo  
RUN yum -y install openssh-server openssh-clients passwd nginx php55u
php55u-mysqlnd php55u-cli php55u-devel php55u-json php55u-gd php55u-pecl-
memcache php55u-pspell php55u-snmp php55u-xmlrpc php55u-xml php55u-fpm
php55u-mbstring tree python-pip  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
RUN pip install "pip>=1.4,<1.5" \--upgrade  
RUN pip install supervisor  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && ssh-keygen -q
-N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
RUN sed -ri 's/GSSAPIAuthentication yes/GSSAPIAuthentication no/g'
/etc/ssh/sshd_config  
RUN useradd developer -u 666  
RUN mkdir /home/developer/.ssh/  
RUN chmod 700 /home/developer/.ssh/  
RUN chown developer:developer /home/developer/.ssh/  
RUN gpasswd -a developer apache  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
ADD conf-nginx.conf /etc/nginx/conf.d/default.conf  
ADD conf-php.conf /etc/php-fpm.d/www.conf  
ADD conf-supervisord.conf /etc/supervisord.conf  
EXPOSE 80  
EXPOSE 22  
ADD run /usr/local/bin/  
RUN chmod +x /usr/local/bin/run  
CMD ["/usr/local/bin/run"]

