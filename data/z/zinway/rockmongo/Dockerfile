FROM centos  
  
MAINTAINER Zinway <z@zin.so>  
  
# update, install required, clean  
RUN yum -y update && yum install -y httpd php php-devel wget php-pear unzip
gcc-c++ make vim git openssl-devel && yum clean all  
  
# update pecl channels  
RUN pecl update-channels  
  
# install mongo drivers without Cyrus SASL (MongoDB Enterprise Authentication)  
RUN printf "no\n" | pecl install mongo && echo "extension=mongo.so" >>
/etc/php.d/mongo.ini  
  
# install RockMongo  
RUN git clone https://github.com/iwind/rockmongo.git /rockmongo \  
&& rm -rf /var/www/html && ln -snf /rockmongo /var/www/html  
  
# increase php upload size  
RUN sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 10M/g'
/etc/php.ini && sed -i 's/post_max_size = 2M/post_max_size = 10M/g'
/etc/php.ini  
  
# copy init script  
COPY run.sh /run.sh  
  
# Expose ports  
EXPOSE 80  
CMD ["/bin/bash", "/run.sh"]  

