FROM ruby:2.3  
ENV RAILS_ENV production  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y postgresql-client --no-install-
recommends && rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev  
RUN apt-get install -y texlive-extra-utils  
RUN apt-get install -y pdftk  
  
RUN export IMAGGA_AUTHORIZATION=$IMAGGA_AUTHORIZATION  
  
RUN mkdir /casemee_core  
WORKDIR /casemee_core  
ADD Gemfile /casemee_core/Gemfile  
ADD Gemfile.lock /casemee_core/Gemfile.lock  
  
RUN gem install bundler  
RUN bundle install --without test development  
  
ADD . /casemee_core  

