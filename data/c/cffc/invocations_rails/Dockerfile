FROM ruby:2.3.1  
RUN apt-get update -qq && apt-get install -y build-essential nodejs npm
nodejs-legacy libpq-dev libmysqlclient-dev  
  
RUN mkdir -p /usr/src/app  
RUN mkdir /usr/src/app/log  
RUN mkdir -p /usr/src/app/tmp/pids  
  
WORKDIR /usr/src/app  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY . /usr/src/app  
RUN bundle exec rake assets:precompile  
EXPOSE 9292  
CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]  

