FROM phusion/passenger-ruby22:0.9.18  
USER root  
  
ENV APP_HOME /home/app/  
  
# Set correct environment variables.  
ENV HOME $APP_HOME  
  
RUN apt-get update && apt-get install unzip  
  
# install Serf  
ADD https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip /tmp/serf.zip  
RUN unzip /tmp/serf.zip -d /usr/local/bin/  
RUN rm /tmp/serf.zip  
  
# add configuration files and handlers for Serf  
COPY serf-config /etc/serf  
RUN mkdir -p /etc/service/serf/  
COPY scripts/serf.run /etc/service/serf/run  
RUN chmod 755 /etc/service/serf/run  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Expose Nginx HTTP service  
EXPOSE 80 443 7946 7373  
# Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD configs/rails-env.conf /etc/nginx/main.d/rails-env.conf  
ADD configs/postgres-env.conf /etc/nginx/main.d/postgres-env.conf  
  
# Facilitates access when utilizing home mount  
RUN usermod -u 1000 -g 50 app  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

