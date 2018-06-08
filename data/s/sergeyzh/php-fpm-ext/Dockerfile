FROM sergeyzh/centos6-php-fpm  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
RUN yum install -y php-xml php-pecl-apc php-pdo php-mysql php-mbstring php-
process php-ldap php-pear sendmail  
  
RUN sed -i "/^wait/i \/sbin/service sendmail start\n" /run-services.sh  
  
# To fix bug on Docker Hub. I hope it will be fixed soon  
RUN chmod g+s /usr/sbin/sendmail.sendmail  
  
RUN yum install -y m4 sendmail-cf cyrus-sasl-plain  
  
ADD pre-run.sh /  
RUN chmod a+x /pre-run.sh  
  
CMD /pre-run.sh  
  
EXPOSE 9000  

