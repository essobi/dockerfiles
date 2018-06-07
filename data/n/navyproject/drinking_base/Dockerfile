FROM ruby:2.1  
WORKDIR /var/www  
  
RUN apt-get -y update  
RUN apt-get -y install git curl build-essential bison openssl libreadline6
libreadline6-dev zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0
libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev
libmysqlclient-dev  
  
ADD Gemfile /var/www/Gemfile  
ADD Gemfile.lock /var/www/Gemfile.lock  
  
RUN bundle install --path=/var/bundler  

