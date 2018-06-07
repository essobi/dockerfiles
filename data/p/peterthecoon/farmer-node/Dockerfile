FROM seapy/rails-nginx-unicorn-pro:v1.0-ruby2.2.0-nginx1.6.0  
MAINTAINER seapy(iamseapy@gmail.com)  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --force-yes libpq-dev  
ENV SQL_HOST 192.168.99.100  
ENV SQL_PORT 32778  
ENV SQL_USERNAME postgres  
ENV SQL_PASSWORD postgres  
ENV SECRET_KEY_BASE mysecret  
ENV REDIS_HOST 192.168.99.100  
ENV REDIS_PORT 32777  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install --without development test  
ADD . /app  
EXPOSE 80  

