FROM ruby:2.2  
MAINTAINER Jérémy SEBAN <jeremy@seban.eu>  
  
ENV APP_HOME /srv/app  
ENV RAILS_ENV production  
  
# Installing nginx  
RUN apt-get update -qq && apt-get install -qq -y nginx nodejs --no-install-
recommends \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copying nginx configuration  
RUN rm -rf /etc/nginx/sites-* /etc/nginx/conf.d  
COPY ./config/dockerized/nginx.conf /etc/nginx/nginx.conf  
  
# Creating application folder  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
# Adding gems dependencies  
ADD ./Gemfile* $APP_HOME/  
RUN echo "gem: --no-rdoc --no-ri" > ~/.gemrc  
RUN bundle install --without development  
  
# Copying application  
ADD . $APP_HOME  
  
# Precompile assets  
RUN bundle exec rake assets:precompile  
  
# Expose HTTP port  
EXPOSE 80  
# Set entrypoint  
# The entrypoint will :  
# - Executes migrations  
# - Starts the puma server of the backend of the app  
# - Starts the nginx server in frontend  
COPY ./config/dockerized/entrypoint.rb /entrypoint  
ENTRYPOINT ["/entrypoint"]  
RUN chmod +x /entrypoint

