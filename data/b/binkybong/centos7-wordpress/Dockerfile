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
php71w-mbstring php71w-mcrypt php71w-mysqlnd php71w-xml php71w-fpm nginx
openssl net-tools wget git curl  
  
RUN mkdir /var/www/html -p  
  
ADD scripts /scripts  
RUN curl -LO http://wordpress.org/latest.tar.gz &&\  
tar xvzf /latest.tar.gz -C /var/www/html --strip-components=1 &&\  
rm /latest.tar.gz &&\  
# chown -R apache:apache /var/www/ &&\  
chmod 755 /scripts/*  
  
EXPOSE 80  
RUN yum -y install nmap  
  
RUN chown -R apache:apache /var/www/html  
  
# Executing supervisord  
CMD ["supervisord", "-n"]  

