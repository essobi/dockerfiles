FROM centos:6.7  
MAINTAINER kwangho "kwangho741@gmail.com"  
# install prerequisite  
RUN yum install -y python-setuptools automake libtool flex bison pkgconfig
gcc-c++ boost-devel libevent-devel zliyub-devel python-devel ruby-devel
openssl-devel wget make git tar && yum clean all  
RUN easy_install supervisor  
  
# install thrift  
ENV thrift_src /tmp/thrift  
RUN mkdir -p $thrift_src && \  
cd $thrift_src && \  
wget http://archive.apache.org/dist/thrift/0.9.0/thrift-0.9.0.tar.gz && \  
tar zxvf thrift-0.9.0.tar.gz && \  
cd thrift-0.9.0 && \  
./configure && \  
make && \  
make install  
  
# install fb303  
RUN cd $thrift_src/thrift-0.9.0/contrib/fb303 && \  
./bootstrap.sh && \  
./configure CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H" && \  
make && \  
make install  
  
# install scribe  
ENV scribe_src /tmp/scribe  
RUN mkdir -p $scribe_src  
RUN git clone https://github.com/facebook/scribe $scribe_src  
RUN cd $scribe_src && \  
./bootstrap.sh --with-boost-filesystem=boost_filesystem && \  
./configure --with-boost-system=boost_system-mt --with-boost-
filesystem=boost_filesystem-mt CPPFLAGS="-DHAVE_INTTYPES_H
-DHAVE_NETINET_IN_H" && \  
make && \  
make install  
  
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/scribed.conf  
RUN ldconfig  
  
RUN cp $scribe_src/examples/scribe_cat /usr/local/bin  
RUN cp $scribe_src/examples/scribe_ctrl /usr/local/bin  
  
RUN mkdir -p /etc/scribed  
RUN cp $scribe_src/examples/example1.conf /etc/scribed/default.conf  
RUN echo "SCRIBED_CONFIG=/etc/scribed/default.conf" >> /etc/sysconfig/scribed  
  
ADD script/scribe.sh /etc/init.d/scribed  
RUN chmod ugo+x /etc/init.d/scribed  
  
# install Nginx  
RUN yum install -y epel-release && yum clean all  
RUN yum install -y nginx  
  
# install PHP7 with fpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN yum install -y php php-devel php-fpm php-opcache php-xml php-pecl-ssh2
php-mcrypt php-mbstring php-pdo php-mysqlnd php-pecl-apcu php-pecl-memcache
php-pecl-memcached php-pecl-redis --enablerepo=remi-php70  
  
# web root.  
RUN mkdir -p /html  
  
RUN rm -rf /etc/nginx/nginx.conf  
RUN rm -rf /etc/nginx/conf.d/default.conf  
RUN rm -rf /etc/php-fpm.d/www.conf  
  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/default.conf /etc/nginx/conf.d/default.conf  
ADD config/www.conf /etc/php-fpm.d/www.conf  
  
ADD config/supervisord.conf /etc/supervisord.conf  
  
EXPOSE 80 443 1463  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

