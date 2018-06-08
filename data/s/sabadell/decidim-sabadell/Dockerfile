FROM ruby:2.4.2  
MAINTAINER david.morcillo@codegram.com  
  
ARG rails_env=production  
ARG secret_key_base=  
  
ENV APP_HOME /code  
ENV RAILS_ENV $rails_env  
ENV SECRET_KEY_BASE $secret_key_base  
  
RUN apt-get update  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash && \  
apt-get install -y nodejs  
  
RUN apt-get install -y postgresql postgresql-client  
  
RUN gem install bundler -v "1.14.6"  
  
ADD Gemfile /tmp/Gemfile  
ADD Gemfile.lock /tmp/Gemfile.lock  
RUN cd /tmp && bundle install  
  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
ADD . $APP_HOME  
  
ENV PASSENGER_NGINX_CONFIG_TEMPLATE /code/nginx.conf.erb  
ENV PASSENGER_LOG_FILE /dev/stdout  
ENV PASSENGER_MAX_POOL_SIZE=5  
CMD bundle exec passenger start  

