# Build from the Ruby 2.4 slim linux image for the base box, which is built on
Debian Jesse.  
FROM ruby:2.4-slim  
LABEL maintainer="William Payne <will@paynelabs.io>"  
  
#Create the directory from which the production code will be hosted  
ENV APP_DIR=/usr/  
# Set the rails environment early on, so that all processes are done with
production settings  
ENV RAILS_ENV=production  
  
# Install the basic dependencies for building rails-based applications  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y tzdata libmysqlclient-dev nodejs curl git build-essential  
  
RUN mkdir -p $APP_DIR  
  
WORKDIR $APP_DIR  
  
# Install rails. If you change this version, specify so in the Gemfile as
well.  
RUN gem install rails -v 5.0.1 --no-rdoc --no-ri  
  
# Create a new rails app, but skip the bundle because we're going to copy a
different Gemfile there.  
RUN rails new camaleon --skip-bundle  
  
# Change the working directory to where the rails root actually is.  
WORKDIR $APP_DIR/camaleon  
  
# Now copy the Gemfile into the container so that we have the correct gem
configuration  
COPY Gemfile ./Gemfile  
# Copy the database settings  
COPY database.yml ./config/  
# Copy the puma settings, which dictate how the web service operates  
COPY puma.rb ./config/  
# Copy an initial schema over  
COPY schema.rb ./db/  
# Production configuration  
COPY production.rb ./config/environments/  
# Finally, copy the application configuration over.  
COPY application.rb ./config/application.rb  
  
# Before installing all of the gems, specify the version of Camaleon we're
using  
RUN sed -i "s|CAMA_VERSION|2.4.5 |g" ./Gemfile  
  
RUN bundle install --without development test -j4  
  
# Generate the Camaleon files  
RUN rails generate camaleon_cms:install  
  
#Configuration file for Camaleon  
COPY system.json ./config/  
  
# Finally, precompile the asset pipeline  
RUN bundle exec rake assets:precompile  
  
# Publish port 8080, because that's the port that nginx-proxy looks for. Be
sure this is configured in your config/puma.rb file if you're recreating this
repo.  
EXPOSE 8080

