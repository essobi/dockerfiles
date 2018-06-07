FROM centos:5  
RUN yum update -y  
  
RUN yum install -y \  
curl gcc make autoconf automake libtool re2c flex bison  
  
# Install Apache 1.3  
RUN cd /usr/local/src && \  
curl -sfLO http://archive.apache.org/dist/httpd/apache_1.3.42.tar.gz && \  
tar -xzf apache_1.3.42.tar.gz && \  
cd apache_1.3.42 && \  
./configure --enable-module=so && \  
make && \  
make install && \  
rm /usr/local/src/apache_1.3.42.tar.gz && \  
rm -rf /usr/local/src/apache_1.3.42 && \  
rm -rf /usr/local/apache/htdocs/* && \  
mkdir /usr/local/apache/htdocs/images  
  
ADD httpd.conf /usr/local/apache/conf/httpd.conf  
  
# Install PHP 4.4.9  
RUN cd /usr/local/src && \  
curl -sfLO http://museum.php.net/php4/php-4.4.9.tar.gz && \  
tar -xzf php-4.4.9.tar.gz && \  
cd php-4.4.9 && \  
./configure --with-mysql --with-apxs=/usr/local/apache/bin/apxs && \  
make && \  
make install && \  
rm /usr/local/src/php-4.4.9.tar.gz && \  
rm -rf /usr/local/src/php-4.4.9  
  
ADD php.ini /usr/local/lib/php.ini  
  
# Install MySQL  
RUN yum install -y mysql-server  
ADD mysql/my.conf /etc/my.conf  
  
RUN cd /usr/local/src && \  
curl -sfLO https://github.com/ericandrewlewis/b2/archive/0.6.2.1.tar.gz && \  
tar -xzf 0.6.2.1.tar.gz -C /usr/local/apache/htdocs --strip-components=1 && \  
rm 0.6.2.1.tar.gz  
  
ADD b2config.php /usr/local/apache/htdocs/b2config.php  
  
# Ensure the PHP runtime user has ownership of everything.  
RUN chown -R nobody:nobody /usr/local/apache/htdocs  
  
ENV B2_SITEURL='http://dockerhost' B2_PATH_SERVER='http://dockerhost' \  
B2_ADMIN_EMAIL='admin@example.com' B2_DBNAME='b2' B2_DBHOST='127.0.0.1' \  
B2_DBUSERNAME='root' B2_DBPASSWORD=''
B2_FILEUPLOAD_REALPATH='/usr/local/apache/htdocs/images' \  
B2_FILEUPLOAD_URL='http://dockerhost/images'  
ADD start-b2.sh /usr/local/bin/start-b2  
  
CMD ["start-b2"]

