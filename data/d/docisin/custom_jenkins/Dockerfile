FROM jenkinsci/blueocean:latest  
USER root  
RUN apk update \  
&& apk add php7 php7-iconv php7-dom php7-mbstring php7-openssl php7-xml
php7-tokenizer php7-xsl php7-phar php7-json php7-xmlwriter php7-fileinfo
php7-pdo php7-session php7-gd php7-mysqli php7-pdo_sqlite php7-sqlite3
php7-pdo_mysql php7-ctype  
WORKDIR /opt  
COPY install_composer.sh .  
RUN ./install_composer.sh  
RUN mkdir /root/.ssh \  
&& ssh-keyscan bitbucket.org > ~/.ssh/known_hosts 2>/dev/null  
RUN addgroup -g 82 -S www-data \  
&& adduser -u 82 -H -D -S -G www-data www-data  
WORKDIR /var/jenkins_home  

