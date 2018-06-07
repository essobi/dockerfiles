FROM million12/nginx-php  
  
RUN yum -y remove iputils  
RUN yum -y install yum-plugin-priorities yum-plugin-fastestmirror  
RUN yum -y update  
  
RUN yum -y install php-devel php-memcached php-curl php-sockets php-mcrypt gcc
libtool git make  
  
# add the soul-soldiers vhost  
ADD docker/site-http /data/conf/nginx/conf.d/soul-soldiers.conf  
  
WORKDIR /tmp  
# Run build process on one line to avoid generating bloat via intermediate
images  
RUN /usr/bin/git clone git://github.com/phalcon/cphalcon.git && \  
cd cphalcon/ && \  
/usr/bin/git checkout phalcon-v1.3.4 && \  
cd build/ && \  
./install && \  
cd /tmp && \  
/bin/rm -rf /tmp/cphalcon/  
  
# add phalcon.ini  
RUN /bin/echo 'extension=phalcon.so' > /etc/php.d/phalcon.ini  
  
ADD . /var/www/soul-soldiers  
  
ADD docker/run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["/run.sh"]

