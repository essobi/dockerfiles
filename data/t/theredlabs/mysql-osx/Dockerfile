FROM mysql  
MAINTAINER Erick Rojas <erick@theredlabs.com>  
COPY ["newentrypoint.sh", "/newentrypoint.sh"]  
ENV MYSQL_USER mysql  
RUN chmod 755 /newentrypoint.sh  
ENTRYPOINT /newentrypoint.sh

