FROM nginx  
MAINTAINER tanner filip <tanner@mozilla-community.org>  
  
# do updates, and install git  
RUN apt-get -y update  
RUN apt-get -y dist-upgrade && apt-get -y install git-core php5-fpm curl  
  
# pull the code  
RUN git clone https://github.com/MozJan/mozillade /var/www/  
COPY mozillade.conf /etc/nginx/conf.d/mozillade.conf  
  
# some configurations  
RUN rm /etc/nginx/conf.d/default.conf  
RUN chown -R nginx:nginx /var/www/  
RUN sed -i s/www-data/nginx/g /etc/php5/fpm/pool.d/www.conf  
COPY startup.sh /root/  
  
ENTRYPOINT ["bash","/root/startup.sh"]  

