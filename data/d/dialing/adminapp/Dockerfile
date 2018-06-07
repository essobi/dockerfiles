FROM ubuntu:16.04  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y software-properties-common locales  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN add-apt-repository -y ppa:ondrej/php  
RUN apt-get update  
  
RUN apt-get install -y nginx php7.2-fpm  
RUN apt-get install -y nginx php7.2 php7.2-mbstring php7.2-dom php7.2-mysql
php7.2-curl php7.2-gd  
  
RUN mkdir /var/www/html/adminapp/  
RUN systemctl enable php7.2-fpm && systemctl enable nginx  
  
ADD . /var/www/html/adminapp/  
COPY deployments/env /var/www/html/adminapp/.env  
COPY deployments/nginx_default.conf /etc/nginx/sites-available/default  
  
RUN sed -i -e "s/try_files/#try_files/g" /etc/nginx/snippets/fastcgi-php.conf
&& \  
sed -i -e "s/pm = dynamic/pm = ondemand/g" /etc/php/7.2/fpm/pool.d/www.conf &&
\  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.2/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/7.2/fpm/php.ini  
  
RUN apt-get autoremove -y software-properties-common  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT service php7.1-fpm start&service nginx start&tail -f /dev/null  

