FROM ruby:2.4.2-slim  
  
RUN apt-get update -qq && \  
apt-get install -y \  
build-essential git \  
postgresql-client libpq-dev \  
libgeos-dev libgeos-3.4.2 curl --no-install-recommends && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ARG RAILS_ENV  
ENV RAILS_ENV $RAILS_ENV  
RUN mkdir -p /app/tmp/pids  
  
WORKDIR /app  
  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install -j 4 --full-index --without development test  
  
ADD package.json /app/package.json  
ADD npm-shrinkwrap.json /app/npm-shrinkwrap.json  
RUN npm install  
RUN webpack --config=config/webpack.config.js  
ADD . /app  
  
RUN rake assets:precompile  
  
CMD puma -C config/puma.rb

