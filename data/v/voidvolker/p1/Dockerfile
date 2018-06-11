FROM ruby:2.5.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev apt-
utils  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get install -y nodejs  
  
ENV PROJECT_ROOT /usr/src/app  
ENV GEM_HOME $PROJECT_ROOT/vendor/bundle  
ENV BUNDLE_PATH $PROJECT_ROOT/vendor/bundle  
ENV BUNDLE_JOBS 2  
RUN mkdir -p $PROJECT_ROOT  
  
WORKDIR $PROJECT_ROOT  
  
COPY Gemfile .  
COPY Gemfile.lock .  
  
RUN bundle install  
  
COPY . .  

