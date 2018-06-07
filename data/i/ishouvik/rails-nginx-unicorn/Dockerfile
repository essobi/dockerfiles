FROM ishouvik/ruby:latest  
MAINTAINER Shouvik Mukherjee <contact@ishouvik.com>  
  
# Install nodejs  
RUN apt-get install -qq -y nodejs  
  
# Install Nginx.  
RUN apt-get install -qq -y nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN chown -R www-data:www-data /var/lib/nginx  
  
# Add default nginx config  
ADD files/config/nginx.conf /etc/nginx/sites-enabled/default  
  
# Install foreman  
RUN gem install foreman  
  
# Add default unicorn config  
ADD files/config/unicorn.rb /app/config/unicorn.rb  
  
# Add default foreman config  
ADD files/Procfile /app/Procfile  
  
# Set Rails environment to production  
ENV RAILS_ENV production  
ENV RACK_ENV production  
  
# Precompile asset and starte foreman  
CMD bundle exec rake assets:precompile && foreman start -f Procfile  
  
# (required) nginx port number  
EXPOSE 80  

