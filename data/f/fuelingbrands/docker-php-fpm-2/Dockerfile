FROM fuelingbrands/docker-php-fpm-2:php7  
  
#------------------------------  
# Install and configure Nginx  
#------------------------------  
RUN apt-add-repository ppa:nginx/stable  
RUN apt-get update && apt-get install -y --force-yes nginx  
  
# Create default app directory  
RUN rm -rf /var/www  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Shell script must run the daemon without letting it daemonize/fork it  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Remove default sites  
RUN rm -rf /etc/nginx/sites-available/* /etc/nginx/sites-enabled/*  
  
# build the daemon  
RUN mkdir /etc/service/nginx  
ADD build/daemons/nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
#------------------------------  
# Add Default Helper Scripts  
#------------------------------  
RUN rm -rf /scripts/*  
COPY build/scripts /scripts  
RUN chmod +x /scripts/*.sh  
  
#------------------------------  
# Add default Nginx settings  
#------------------------------  
COPY build/nginx /nginx-configs  
  
#------------------------------  
# Add init commands  
#------------------------------  
COPY build/commands /commands  
  
#------------------------------  
# Finish and Cleanup  
#------------------------------  
EXPOSE 80  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

