FROM ruby:2.3.7-jessie  
LABEL maintainer="Ivan Ivanov csyntax@outlook.com"  
ENV RAILS_ENV production  
RUN apt-get update && apt-get install -y build-essential nodejs-legacy sqlite3
libsqlite3-dev libv8-dev git-core redis-server  
RUN gem install libv8 -v '3.11.8.17' \-- --with-system-v8  
#gem install therubyracer -v 0.11.0 # -v 0.12  
RUN mkdir /var/app  
WORKDIR /var/app  
COPY . /var/app  
RUN bundle install  
RUN bundle exec rake assets:precompile  
RUN bundle exec rake db:migrate  
RUN bundle exec rake db:seed  
RUN redis-server --daemonize yes  
  
CMD bundle exec puma -C config/puma.rb  
EXPOSE 5000  

