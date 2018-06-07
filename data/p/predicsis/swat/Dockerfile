FROM ruby:2.2.2  
MAINTAINER HugoPouliquen  
  
ENV RAILS_ENV production  
ENV LANG C.UTF-8  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN mkdir -p tmp/pids  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install --deployment --jobs=8 --retry=3 --without development test  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]  

