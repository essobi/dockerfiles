FROM centos:centos6  
  
# Installing base components  
RUN yum -y update && yum -y install wget curl unzip supervisor g++ make mc vim
tar gcc pcre-devel openssl-devel patch libmcrypt-devel libxml2-devel
bzip2-devel libcurl-devel readline-devel git && yum clean all  
  
RUN groupdel games && groupadd -g 20 www-data && useradd -g www-data -u 502 -M
-d /var/www/html www-data  

