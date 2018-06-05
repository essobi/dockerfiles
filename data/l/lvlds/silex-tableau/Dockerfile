FROM centos:6  
RUN mkdir /app  
RUN yum -y update && yum clean all  
RUN yum install -y gcc git httpd php php-devel php-ldap php-pear zlib-devel
pcre-devel  
  
RUN pecl install propro-1.0.0 && echo "extension=propro.so" >
/etc/php.d/propro.conf \  
pecl install raphf-1.0.2 && echo "extension=raphf.so" > /etc/php.d/raphf.conf
\  
pecl install pecl_http-2.0.4 && echo "extension=http.so" >
/etc/php.d/http.conf  
  
WORKDIR /tmp  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php --install-dir=/usr/bin --filename=composer  
RUN php -r "unlink('composer-setup.php');"  
  
WORKDIR /app/  
  
EXPOSE 80

