FROM ruby:2.2  
MAINTAINER Secret Sauce Partners, Inc. <dev@sspinc.io>  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
# create directory for app  
RUN mkdir -p /app  
WORKDIR /app  
  
# install node and psql  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/* && gem install foreman  
  
# add gemfile and install dependencies  
ADD Gemfile Gemfile.lock /app/  
RUN bundle install --without development test  
  
# set production environment  
ENV RACK_ENV=production HOME=/app  
  
# Add application files  
ADD . /app  
  
# precompile assets  
RUN bundle exec rake assets:precompile  
  
EXPOSE 5000  
CMD ["foreman", "start"]  

