FROM phusion/passenger-ruby22:latest  
MAINTAINER Michael Kirk <michael@jackpine.me>  
  
ENV HOME /root  
  
CMD ["/sbin/my_init"]  
  
RUN rm /etc/service/nginx/down  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD config/containers/api/conf/collision-api.conf /etc/nginx/sites-
enabled/collision-api.conf  
  
# Don't re-run bundle install unless Gemfile changes - otherwise if we do it  
# *after* we add the app, we'll run bundle install everytime any file in the  
# app changes. Copy the Gemfile and Gemfile.lock into the image.  
# Temporarily set the working directory to where they are.  
WORKDIR /tmp  
ADD Gemfile /tmp/Gemfile  
ADD Gemfile.lock /tmp/Gemfile.lock  
RUN bundle install  
  
RUN mkdir /home/app/collision  
ADD . /home/app/collision/api  
# Copy over template env file  
ADD .env-template /home/app/collision/api/.env  
  
RUN chown -R app:app /home/app/collision  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

