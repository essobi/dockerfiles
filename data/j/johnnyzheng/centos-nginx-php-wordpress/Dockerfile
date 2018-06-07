FROM johnnyzheng/centos-nginx-php  
MAINTAINER Johnny Zheng <johnny@itfolks.com.au>  
  
RUN curl https://wordpress.org/latest.tar.gz | tar xz  
RUN curl -o /usr/local/bin/wp https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar && chmod +x /usr/local/bin/wp  
#RUN curl https://github.com/wp-cli/wp-cli/raw/master/utils/wp-completion.bash
| source && source ~/.bash_profile  
ADD container-files /  
RUN cd /wordpress && chown www:www . -R && find . -type d -exec chmod 700 {}
\; && find . -type f -exec chmod 600 {} \; && chmod -R 777 wp-content  
  
# Exposed ENV  
ENV DOMAIN="" LOCALE="zh_CN" TIMEZONE="Asia/Shanghai" TITLE="Wordpress"
ADMIN_EMAIL="admin@localhost" ADMIN_PASSWORD="password" DB_ENV_USER="admin"
DB_ENV_PASS="" OVERRIDDEN="FALSE"  

