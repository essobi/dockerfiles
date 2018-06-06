# use centos latest image  
FROM centos:centos6  
  
# update the packages  
RUN yum update -y  
  
# install epel and webtatic repositories  
RUN yum install -y epel-release && rpm -Uvh
https://mirror.webtatic.com/yum/el6/latest.rpm  
  
# install php and development tools  
RUN yum install -y \  
php56w \  
php56w-common \  
php56w-cli \  
php56w-gd \  
php56w-mcrypt \  
php56w-mysql \  
php56w-pdo \  
php56w-soap \  
php56w-xml \  
php56w-mbstring \  
git \  
vim \  
tar \  
npm \  
&& yum groupinstall -y "Development Tools"  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/bin
--filename=composer  
  
# install php code sniffer  
RUN composer global require "squizlabs/php_codesniffer=*"  
# install php mess detector  
RUN composer global require "phpmd/phpmd=*"  
# install semistandard  
RUN npm install -g semistandard  
  
# make sure composer vendors are in PATH  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
# create web host directory  
RUN rm -rf /var/www && mkdir -p /var/www  
  
# set working directory to that of the web host  
WORKDIR /var/www  
  
# command to un on running of container with no arguments  
CMD bash  

