FROM hipflat/common  
MAINTAINER Roonglit Chareonsupkul <roonglit@gmail.com>  
  
# install dependencies  
RUN apt-get install -qy software-properties-common memcached  
  
# install libs for htpasswd  
RUN apt-get install -qy apache2-utils  
  
# install nginx  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -qy nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# add default nginx config  
ADD nginx-sites.conf /etc/nginx/sites-enabled/default  
  
# set up app folder  
WORKDIR /app  
  
# add configuration for monit  
ADD ./monit_nginx /etc/monit/conf.d/nginx  
ADD ./monit_puma /etc/monit/conf.d/puma  
  
# add default puma config  
ADD puma.rb /app/config/puma.rb  
  
ENV RAILS_ENV production  
  
# add default supervisor config  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# add start-app script for Puma  
ADD start-app.sh /usr/bin/start-app  
RUN chmod +x /usr/bin/start-app  

