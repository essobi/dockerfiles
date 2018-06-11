FROM wwek/centos:7  
  
LABEL version="1.0" \  
description="Language:PHP7 Golang Nodejs Python3 Java" \  
maintainer="wwek<licoolgo@gmail.com>"  
# Install base  
RUN yum makecache && yum update -y \  
&& yum groupinstall "Development Tools" -y \  
&& yum install nodejs -y \  
&& yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel -y \  
&& yum clean all && rm -rf /var/cache/yum/  
# Install PHP71  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \  
&& yum install php71w-cli -y \  
&& yum install php71w-fpm -y \  
&& yum install php71w-gd -y \  
&& yum install php71w-mbstring -y \  
&& yum install php71w-mcrypt -y \  
&& yum install php71w-mysqlnd -y \  
&& yum install php71w-pdo -y \  
&& yum install php71w-pear -y \  
&& yum install php71w-pecl-redis -y \  
&& yum install php71w-pecl-xdebug -y \  
&& yum install php71w-xml -y \  
&& yum install php71w-xmlrpc -y \  
&& yum install php71w-opcache -y \  
&& yum clean all && rm -rf /var/cache/yum/  
# Install PHP Composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.5.2  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
\  
&& php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& composer --ansi --version --no-interaction \  
&& rm -rf /tmp/* /tmp/.htaccess  
# Install Golang1.9.2  
RUN wget --no-check-certificate
https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz \  
&& tar zxvf go1.9.2.linux-amd64.tar.gz -C /usr/local/ \  
&& mkdir -p /data/go \  
&& rm -rf go1.9.2.linux-amd64.tar.gz  
ENV GOROOT /usr/local/go  
ENV GOBIN $GOROOT/bin  
ENV GOPATH /data/go  
ENV PATH $PATH:$GOBIN:$GOPATH/bin  
  
# 挂载目录  
VOLUME /data  
  
# 开放开发常用端口  
EXPOSE 22  
EXPOSE 80  
EXPOSE 81  
EXPOSE 88  
EXPOSE 443  
EXPOSE 3306  
EXPOSE 8080  
EXPOSE 8081  
# bash  
#CMD ["/bin/bash"]  
# 入口设置为ssh  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]

