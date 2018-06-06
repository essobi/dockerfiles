FROM centos:7  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \  
&& yum install -y httpd php70w php70w-common php70w-pdo php70w-mbstring \  
&& yum clean all \  
&& curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/local/bin --filename=composer  
  
COPY ./vhost.conf /etc/httpd/conf.d/welcome.conf  
WORKDIR /var/www/html  
  
COPY ./composer.json .  
COPY ./composer.lock .  
RUN composer install --no-autoloader --no-scripts --no-dev  
  
COPY . .  
  
RUN composer install --optimize-autoloader --no-dev \  
&& composer dump-autoload --optimize \  
&& chown -R apache:apache /var/www/html  
  
ENV SERVER_NAME="www.example.com"  
ENV SERVER_ADMIN="example@example.com"  
ENV DB_CONNECTION="mysql"  
ENV DB_HOST="127.0.0.1"  
ENV DB_DATABASE="homestead"  
ENV DB_USERNAME="homestead"  
ENV DB_PASSWORD="secret"  
ENV CACHE_DRIVER="file"  
ENV SESSION_DRIVER="file"  
ENV QUEUE_DRIVER="sync"  
ENV REDIS_HOST="127.0.0.1"  
ENV REDIS_PASSWORD="null"  
ENV REDIS_PORT="6379"  
ENV MAIL_DRIVER="smtp"  
ENV MAIL_HOST="mailtrap.io"  
ENV MAIL_PORT="2525"  
ENV MAIL_USERNAME="null"  
ENV MAIL_PASSWORD="null"  
ENV MAIL_ENCRYPTION="null"  
EXPOSE 80  
COPY dockerlaravel /usr/local/bin/  
RUN chmod 777 /usr/local/bin/dockerlaravel  
ENTRYPOINT dockerlaravel

