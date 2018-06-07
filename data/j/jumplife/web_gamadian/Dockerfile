# FROM ruby:2  
FROM phusion/passenger-ruby22:0.9.19  
ENV HOME /root  
  
# Set the timezone.  
RUN rm /etc/timezone  
RUN echo "Asia/Taipei" > /etc/timezone  
RUN rm /etc/localtime  
RUN echo "Asia/Taipei" > /etc/localtime  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
# Init  
RUN apt-get update && apt-get install -y \  
build-essential \  
libpq-dev \  
nodejs  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
# Nginx / Passenger  
# Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# Add the nginx info  
ADD nginx.conf /etc/nginx/sites-enabled/app.conf  
  
# Rails  
# Add the rails-env configuration file  
ADD rails-env.conf /etc/nginx/main.d/rails-env.conf  
  
# Run Bundle in a cache efficient way  
WORKDIR /app  
ADD . /app  
ADD Gemfile /app/  
ADD Gemfile.lock /app/  
RUN chmod -R 777 /app  
RUN bundle install --jobs 8 --retry 5  
RUN RAILS_ENV=production bundle exec rake assets:precompile  
RUN RAILS_ENV=production bundle exec whenever --update-crontab  
  
EXPOSE 80  
# EXPOSE 3000  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
# CMD ["rails", "server"]

