#
=============================================================================  
# solodev/centos-php56  
#  
# CentOS-7, Open SSL, PHP 5.6 (Tidy, Mongo, Zip, Pecl, Soap), Python PIP, ZIP,
REDIS, Node, NPM  
# Used for Bitbucket Pipelines  
# Keeping the love for CentOS  
#  
#
=============================================================================  
FROM centos:centos7  
  
MAINTAINER Solodev <info@solodev.com>  
#docker build -t="solodev/centos-php56" .  
#docker exec -it "centos" bash  
#docker run -i -t centos  
#Cleanup Scripts  
#docker rm -f $(docker ps -a -q)  
#docker rmi $(docker images -q -f dangling=true)  
#docker rmi -f $(docker images -q)  
#
-----------------------------------------------------------------------------  
# Import the RPM GPG keys for Repositories  
#
-----------------------------------------------------------------------------  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
RUN yum -y install epel-release  
RUN yum -y update  
  
#
-----------------------------------------------------------------------------  
# UTC Timezone & Networking  
#
-----------------------------------------------------------------------------  
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime \  
&& echo "NETWORKING=yes" > /etc/sysconfig/network  
  
#
-----------------------------------------------------------------------------  
# SSL  
#
-----------------------------------------------------------------------------  
RUN yum --setopt=tsflags=nodocs -y install \  
unzip \  
mod_ssl \  
openssl-devel \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
#
-----------------------------------------------------------------------------  
# PHP  
#
-----------------------------------------------------------------------------  
RUN yum --setopt=tsflags=nodocs -y install \  
php56w \  
php56w-cli \  
php56w-mysql \  
php56w-pdo \  
php56w-mbstring \  
php56w-soap \  
php56w-gd \  
php56w-xml \  
php56w-pecl-apcu \  
php56w-tidy \  
php56w-soap \  
php56w-devel \  
php56w-pear \  
pcre-devel \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
RUN yum install -y gcc \  
gcc-c++ \  
make \  
zip  
  
#
-----------------------------------------------------------------------------  
# Install Python PIP  
#
-----------------------------------------------------------------------------  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"  
RUN python get-pip.py  
RUN pip install boto3==1.3.0  
  
#
-----------------------------------------------------------------------------  
# Install PHP Mongo  
#
-----------------------------------------------------------------------------  
RUN printf "\n" | pecl install mongodb  
RUN echo "extension=mongodb.so" >> /etc/php.d/mongodb.ini  
  
#
-----------------------------------------------------------------------------  
# Install REDIS  
#
-----------------------------------------------------------------------------  
RUN yum -y install redis  
RUN chkconfig redis on  
USER root  
VOLUME ["/var/lib/redis"]  
ENV HOME /var/lib/redis  
WORKDIR /var/lib/redis  
CMD ["/usr/bin/redis-server", "/etc/redis.conf"]  
EXPOSE 6379  
#
-----------------------------------------------------------------------------  
# Install Node  
#
-----------------------------------------------------------------------------  
RUN yum -y install npm  
RUN npm cache clean -f  
RUN npm install -g n  
RUN n stable

