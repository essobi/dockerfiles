FROM centos:7  
LABEL maintainer="Sander van Dinten <sander@vandinten.nl>"  
  
RUN yum -y update && \  
yum -y install httpd php-gd php-curl php-gmp php-mysql php \  
php-mbstring php-xml && \  
yum clean all && \  
curl https://codeload.github.com/spotweb/spotweb/tar.gz/master | \  
tar -zx -C /var/www/html -f - && \  
mv /var/www/html/spotweb-master /var/www/html/spotweb  
  
ENV SPOT_WEB_TZ='Europe/Amsterdam'  
COPY ownsettings.php /  
COPY docker-entrypoint.sh /  
  
EXPOSE 80  
VOLUME /var/www/html/spotweb/cache  
  
ENTRYPOINT /docker-entrypoint.sh  

