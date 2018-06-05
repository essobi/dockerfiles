FROM ubuntu  
MAINTAINER BloomBoard Team tech@bloomboard.com  
# Adapted from clue/webgrind  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
nginx supervisor php5-fpm php5-cli \  
graphviz python \  
git  
  
# add webgrind as the only nginx site  
ADD webgrind.nginx.conf /etc/nginx/sites-available/webgrind  
RUN ln -s /etc/nginx/sites-available/webgrind /etc/nginx/sites-
enabled/webgrind  
RUN rm /etc/nginx/sites-enabled/default  
  
# install webgrind from git  
RUN git clone https://github.com/jokkedk/webgrind /var/webgrind  
RUN chown www-data:www-data -R /var/webgrind  
  
ADD config.php /var/webgrind/config.php  
  
# expose only nginx HTTP port  
EXPOSE 80  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  

