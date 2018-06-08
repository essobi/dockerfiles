FROM ruby:2.3.3-slim  
  
MAINTAINER thecdx <admin@thecdx.org>  
  
RUN apt-get update && apt-get install -y --no-install-recommends build-
essential nodejs nginx git imagemagick libmysqlclient-dev && rm -rf
/var/lib/apt/lists/* \  
&& echo "\ndaemon off;" >> /etc/nginx/nginx.conf && chown -R www-data:www-data
/var/lib/nginx  
  
ENV RAILS_ENV production  
  
# Add default nginx config  
ADD nginx-sites.conf /etc/nginx/sites-enabled/default  
  
# Install foreman  
RUN gem install foreman  
  
COPY *.rb /app/config/  
  
# Install app  
WORKDIR /app  
ONBUILD COPY ["Gemfile", "Gemfile.lock", "/app/"]  
ONBUILD ADD . /app  
ONBUILD RUN bundle install --without development test \--jobs 8  
ONBUILD RUN bundle exec rake assets:precompile  
  
EXPOSE 80  
EXPOSE 443  

