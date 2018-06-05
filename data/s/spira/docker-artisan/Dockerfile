FROM spira/docker-base  
  
MAINTAINER "Zak Henry" <zak.henry@gmail.com>  
  
RUN apt-get update -y && \  
apt-get install -y \  
php5-cli \  
php5-mcrypt \  
php5-curl \  
php5-mongo \  
php5-mssql \  
php5-mysqlnd \  
php5-pgsql \  
php5-redis \  
php5-sqlite \  
php5-gd  
  
RUN mkdir -p ${DATA_ROOT:-/data}${API_PATH:-/api}  
#todo change WORKDIR to ${DATA_ROOT:-/data} syntax when supported  
WORKDIR ${DATA_ROOT}${API_PATH}  
  
ENTRYPOINT ["php", "artisan"]  
CMD ["--help"]  

