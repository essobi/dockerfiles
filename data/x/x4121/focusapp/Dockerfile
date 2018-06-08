FROM ruby:2.3  
MAINTAINER Armin Grodon <me@armingrodon.de>  
  
RUN apt-get update \  
&& apt-get install -y sqlite3 nodejs \  
&& rm -rf /var/lib/lists/* \  
&& git clone https://github.com/x4121/focusapp \  
&& cd focusapp \  
&& sed -i "s/mysql2.*$/sqlite3'/" Gemfile \  
&& bundle install \  
&& sed -i \  
"/username:/d;/password:/d;/host:/d;/socket:/d;s/mysql2/sqlite3/;s/focusapp_development/db\/development.sqlite3/;s/focusapp_test/db\/test.sqlite3/;s/focusapp_production/db\/production.sqlite3/"
\  
config/database.yml \  
&& rails db:migrate db:seed  
  
WORKDIR /focusapp  
  
EXPOSE 3000  
CMD ["rails", "server", "-b", "0.0.0.0"]  

