FROM odaniait/passenger-docker:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
# Workaround for hash sum mismatch
http://forum.siduction.org/index.php?topic=4294.0  
RUN rm -rf /var/lib/apt/lists  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# Prepare folders  
RUN mkdir /home/app/webapp  
  
# Add the rails app  
ADD . /home/app/webapp  
  
# Add mongoid environment file for nginx  
ADD docker/mongoid-env.conf /etc/nginx/main.d/mongoid-env.conf  
  
WORKDIR /home/app/webapp  
RUN chown -R app:app /home/app/webapp  
RUN MONGODB_1_PORT_27017_TCP_ADDR=127.0.0.1
MONGODB_1_PORT_27017_TCP_PORT=27017 bundle install  
RUN MONGODB_1_PORT_27017_TCP_ADDR=127.0.0.1
MONGODB_1_PORT_27017_TCP_PORT=27017 bundle exec rake assets:precompile  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

