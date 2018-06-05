# Centos 7  
FROM centos:centos7  
  
MAINTAINER Andy Wong <pslandywong@hotmail.com>  
  
ADD /contents /  
  
RUN yum -y install epel-release  
  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
RUN yum -y update &&\  
yum clean all  
  
# Installing supervisor  
RUN yum install -y python-setuptools  
  
RUN easy_install pip  
  
RUN pip install supervisor  
  
RUN yum install -y mod_php71w php71w-cli php71w-common php71w-gd
php71w-mbstring php71w-mcrypt php71w-mysqlnd php71w-xml php71w-fpm
php71w-pgsql nginx openssl net-tools wget git curl  
  
RUN mkdir /var/www/html -p  
  
RUN mkdir /etc/letsencrypt -p  
  
EXPOSE 80 443  
RUN chown -R apache:apache /var/www/html  
  
# Executing supervisord  
CMD ["supervisord", "-n"]  

