FROM maxexcloo/nginx-php:latest  
MAINTAINER Max Schaefer <max@excloo.com>  
  
ENV VERSION 5.1  
  
ENV POSTGRESQL_HOST=postgresql  
ENV POSTGRESQL_PORT=5432  
ENV POSTGRESQL_DEFAULT_DB=pg  
  
RUN apt-get update && apt-get install -y wget && apt-get clean  
  
RUN mkdir -p /data/http && \  
cd /data/http && \  
wget -O -
"http://www.sourceforge.net/projects/phppgadmin/files/phpPgAdmin%20%5Bstable%5D/phpPgAdmin-${VERSION}/phpPgAdmin-${VERSION}.tar.gz/download"
| tar \--strip-components=1 -x -z && \  
rm -rf conf/config.inc.php-dist CREDITS DEVELOPERS FAQ HISTORY INSTALL TODO
TRANSLATORS  
ADD data /data  

