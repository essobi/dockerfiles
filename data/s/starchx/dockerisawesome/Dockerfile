FROM centos:centos7  
  
MAINTAINER BLAH  
  
# set proxy for yum  
#RUN echo "proxy=http://10.244.9.160:80" | tee -a /etc/yum.conf  
# add epel/webtatic repository and gpg key  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \  
yum -y update  
  
# install php and various extensions  
RUN yum -y install php70w \  
php70w-common \  
php70w-mysql \  
php70w-xml \  
php70w-mbstring \  
php70w-pdo \  
php70w-devel \  
php70w-mcrypt \  
php70w-soap \  
php70w-cli \  
php70w-opcache && \  
yum clean all  
  
# Install php composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv /composer.phar /usr/bin/composer \  
&& chmod +x /usr/bin/composer  
  
CMD ["/bin/bash"]

