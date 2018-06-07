FROM hnakamur/centos:6.5  
#RUN apt-get update && apt-get install -yq git && rm -rf /var/lib/apt/lists/*  
#RUN yum install -y httpd bridge-utils libcurl3-openssl-dev php5-dev  
#RUN yum -y update && yum clean all  
RUN yum -y install httpd bridge-utils && yum clean all  
  
EXPOSE 80  
#RUN pecl -q install raphf  
#RUN pecl -q install propro  
#RUN echo "extension=raphf.so" >> /etc/php5/apache2/php.ini  
#RUN echo "extension=propro.so" >> /etc/php5/apache2/php.ini  
#RUN pecl -q install pecl_http-1.7.6  
#RUN echo "extension=http.so" >> /etc/php5/apache2/php.ini  
#RUN touch /usr/hoge.txt  
#CMD /etc/rc.d/init.d/httpd start  
#RUN chkconfig httpd on  
RUN echo "<PRE>" > /var/www/html/index.html  
RUN cat /etc/redhat-release >> /var/www/html/index.html  
RUN cat /etc/issue >> /var/www/html/index.html  
RUN uname -r >> /var/www/html/index.html  
RUN cat /proc/version >> /var/www/html/index.html  
RUN echo "</PRE>" >> /var/www/html/index.html  
  
CMD /usr/sbin/apachectl -D FOREGROUND  
  

