FROM ruby:2.5.1  
ENV APP_HOME=/home/toolbox  
  
RUN apt-get update \  
&& apt-get install -y git less strace htop siege netcat \  
mariadb-client-10.1 apache2-utils  
  
WORKDIR $APP_HOME  
  
# Install dependencies defined in Gemfile.  
COPY Gemfile Gemfile.lock $APP_HOME/  
RUN mkdir -p /opt/vendor/bundle \  
&& bundle install --path /opt/vendor/bundle  
  
# Copy application sources.  
COPY . $APP_HOME  

