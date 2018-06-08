FROM zimmobe/php:5.5-apache-oraclelinux  
  
RUN yum install -y gcc php55w-devel make \  
&& pecl install xhprof-beta \  
&& echo "extension=xhprof.so" > /etc/php.d/xhprof.ini \  
&& yum remove -y gcc php55w-devel make \  
&& yum autoremove -y \  
&& yum clean all  
  
RUN git clone https://github.com/perftools/xhgui.git /var/www/xhgui \  
&& cd /var/www/xhgui \  
&& php install.php

