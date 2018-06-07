FROM php:7.2-apache-stretch  
  
ENV VERSION=17.4  
ENV DB_TYPE mysql  
ENV DB_HOST localhost  
ENV DB_PORT 3306  
ENV DB_USER ttrss  
ENV DB_PASS ttrss  
ENV DB_NAME ttrss  
  
ENV SELF_URL_PATH ttrss.example.com  
ENV ENABLE_REGISTRATION false  
ENV REG_NOTIFY_ADDRESS 'root@localhost'  
ENV REG_MAX_USERS 10  
ENV SESSION_COOKIE_LIFETIME 86400  
ENV SMTP_SERVER ''  
ENV SMTP_LOGIN ''  
ENV SMTP_PASSWORD ''  
ENV SMTP_SECURE ''  
ENV SMTP_FROM_NAME Tiny Tiny RSS  
ENV SMTP_FROM_ADDRESS no-reply@ttrss.example.com  
ENV DIGEST_SUBJECT [tt-rss] New headlines for last 24 hours  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN docker-php-ext-install \  
mysqli \  
pdo \  
pdo_mysql  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y mariadb-client libmcrypt-dev  
RUN curl -L "https://git.tt-rss.org/git/tt-rss/archive/${VERSION}.tar.gz" >
/ttrss.tar.gz \  
&& tar -xav -C /var/www -f /ttrss.tar.gz \  
&& rm -rf /var/www/html \  
&& mv /var/www/tt-rss* /var/www/html \  
&& chown -R root:root /var/www/html  
RUN apt-get autoremove --purge -y \  
&& rm -rf /var/lib/apt/lists/* /ttrss.tar.gz  
  
COPY assets/config.php /var/www/html/config.php  
COPY entrypoint.sh /  
  
VOLUME "/var/www/html/feed-icons"  
VOLUME "/var/www/html/lock"  
VOLUME "/var/www/html/cache"  
  
ENTRYPOINT [ \  
"/bin/bash", \  
"/entrypoint.sh" \  
]  

