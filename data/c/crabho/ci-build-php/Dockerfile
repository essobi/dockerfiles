FROM debian:jessie  
RUN apt-get update && apt-get install -y --no-install-recommends \  
make \  
curl \  
openssh-client \  
ca-certificates \  
php5-cli \  
php5-curl \  
php5-xsl \  
php-pear \  
php5-dev && \  
rm -rf /var/lib/apt/lists/*  
RUN pecl install xdebug  
RUN echo "zend_extension=/usr/lib/php5/20131226/xdebug.so\n" >>
/etc/php5/cli/php.ini  
  
#COPY ./cert/*.crt /usr/local/share/ca-certificates/  
#RUN chmod 644 /usr/local/share/ca-certificates/* && update-ca-certificates  
# Build git 2.7.4  
RUN curl https://www.kernel.org/pub/software/scm/git/git-2.7.4.tar.gz >
/tmp/git-2.7.4.tar.gz  
RUN cd /tmp && tar -zxvf git-2.7.4.tar.gz  
RUN cd /tmp/git-2.7.4 && \  
./configure --without-tcltk && \  
make -i && \  
make install -i  
RUN cd /tmp && rm -rf git-2.7.4*  
  
RUN php -r "readfile('https://getcomposer.org/installer');" | php --
--install-dir=/usr/local/bin --filename=composer  

