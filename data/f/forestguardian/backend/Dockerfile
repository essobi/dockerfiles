# Explicitely indicate the mainteiner 'library'.  
FROM library/ruby:2.3.3  
# Set rails environment to production.  
RUN export RAILS_ENV=production  
# TODO: Better lock versions.  
RUN apt-get update && apt-get install -y build-essential libpq-dev nodejs
imagemagick --no-install-recommends  
# Free space used by apt-get.  
RUN rm -rf /var/lib/apt/lists/*  
RUN mkdir /ForestGuardianBackend  
WORKDIR /ForestGuardianBackend  
# First copy the Gemfile and Gemfile.lock so bundle install does not run every
time there is a change in the rest of the  
# code.  
COPY Gemfile /ForestGuardianBackend  
COPY Gemfile.lock /ForestGuardianBackend  
# Install gems.  
RUN bundle install  
# Copy code files.  
COPY . /ForestGuardianBackend  
  
ARG RAILS_ENV  
ARG AWS_ACCESS_KEY_ID  
ARG AWS_ACCESS_KEY_KEY  
ARG AWS_REGION  
  
RUN DB_ADAPTER=nulldb rake assets:precompile

