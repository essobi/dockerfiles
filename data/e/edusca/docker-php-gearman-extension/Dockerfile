FROM edusca/docker-nginx-fpm-php5.6  
#install gearman extension  
RUN apt-get update  
RUN apt-get install -y php5.6-dev  
RUN apt-get install -y libgearman-dev  
RUN cd /tmp  
RUN curl -O https://pecl.php.net/get/gearman-1.1.2.tgz  
RUN tar -xzvf gearman-1.1.2.tgz  
RUN cd gearman-1.1.2 && phpize && ./configure && make && make install  
RUN mkdir /usr/lib/php/5.6/extensions  
RUN mv gearman-1.1.2/modules/gearman.so /usr/lib/php/5.6/extensions/gearman.so  
RUN echo "extension=/usr/lib/php/5.6/extensions/gearman.so" >>
/etc/php/5.6/cli/php.ini  
  
#install supervisor and run the deamon  
RUN apt-get install -y supervisor  
RUN service supervisor start  

