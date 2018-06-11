# DOCKER-VERSION 1.6.0, build 4749651  
# habd.as Dockerfile  
# Runs Jekyll under Nginx with Passenger  
FROM phusion/passenger-ruby21:0.9.15  
MAINTAINER Josh Habdas "jhabdas@gmail.com"  
# Set environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init process  
CMD ["/sbin/my_init"]  
  
# Expose Nginx HTTP service  
EXPOSE 80  
# Start Nginx/Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Remove default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# Add Nginx site and config  
COPY nginx.conf /etc/nginx/sites-enabled/webapp.conf  
  
# Install gems  
WORKDIR /tmp  
COPY Gemfile /tmp/  
COPY Gemfile.lock /tmp/  
RUN bundle install  
  
# Add the Passenger app  
COPY . /home/app/webapp  
RUN chown -R app:app /home/app/webapp  
  
# Build app with Jekyll  
WORKDIR /home/app/webapp  
RUN jekyll build  
  
# Clean up APT when done  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

