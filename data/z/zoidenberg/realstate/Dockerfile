FROM phusion/passenger-ruby24:latest  
  
ENV LANG C.UTF-8  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
mysql-client libmysqlclient-dev nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
ENV RAILS_ENV production  
  
COPY Gemfile .  
COPY vendor/cache/ ./vendor/cache/  
  
RUN gem install bundler  
  
RUN bundle install --local \--binstubs  
  
COPY . .  
COPY docker-env/production/database.yml ./config/database.yml  
COPY docker-env/production/secrets.yml ./config/secrets.yml  
  
RUN rm /etc/nginx/sites-enabled/default  
COPY docker-env/production/default /etc/nginx/sites-enabled/default  
  
RUN rm -f /etc/service/nginx/down  

