FROM gregory90/nginx:1.9.1  
  
RUN apt-get update && \  
apt-get install -y php5-cli php5-curl php5-fpm php5-gd php5-mcrypt php5-mysql
php5-sqlite php5-intl php5-redis supervisor && \  
mkdir -p /code && \  
mkdir -p /data/logs && \  
rm -rf /etc/php5/fpm/pool.d  
  
RUN apt-get install -y python-setuptools  
RUN easy_install pip  
RUN pip install supervisor-stdout  
ADD supervisor_stdout.py /usr/local/lib/python2.7/dist-
packages/supervisor_stdout.py  
  
ADD php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD pool.d /etc/php5/fpm/pool.d  
ADD default /etc/nginx/sites-available/default  
ADD default /etc/nginx/sites-enabled/default  
ADD php.ini /etc/php5/fpm/php.ini  
ADD php-cli.ini /etc/php5/cli/php.ini  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD index.php /code/index.php  
  
WORKDIR /code  
  
EXPOSE 3000  
  
CMD ["supervisord"]  
  

