FROM ruby:2.3.1-alpine  
MAINTAINER Darwin Walters <darwin.s.walters@gmail.com>  
  
RUN apk update && apk add build-base nodejs sqlite-dev libgcrypt-dev libxslt-
dev  
  
ENV INSTALL_PATH /dswliftlog  
  
RUN mkdir -p $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY Gemfile Gemfile  
  
# RUN bundle update  
RUN bundle config build.nokogiri --use-system-libraries  
RUN bundle install  
  
RUN bundle update mini_portile2  
  
# RUN export SECRET_KEY_BASE=$(rake secret)  
ENV SECRET_KEY_BASE $(openssl rand -hex 64)  
COPY . .  
  
# RUN bundle exec rake RAILS_ENV=production  
RUN RAILS_ENV=production rake assets:precompile  
# CMD rails s --environment development  

