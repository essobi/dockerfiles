# Use the docker hub ruby image as a base.  
# More on this image here: https://hub.docker.com/_/rails/  
FROM ruby:2.3.0  
# Update and install stuff your app needs to run  
RUN apt-get update -qq  
RUN apt-get install -y build-essential curl git imagemagick libmagickwand-dev
libcurl4-openssl-dev nodejs postgresql-client rsync  
  
# update bundler to avoid this issue on running foreman:
https://github.com/bundler/bundler/issues/4381  
RUN gem update bundler  
  
# Installing your gems this way caches this step so you dont have to reintall
your gems every time you rebuild your image.  
# More info on this here: http://ilikestuffblog.com/2014/01/06/how-to-skip-
bundle-install-when-deploying-a-rails-app-to-docker/  
# Copy the Gemfile and Gemfile.lock into the image.  
# Temporarily set the working directory to where they are.  
WORKDIR /tmp  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN bundle install  
  
# Add our source files precompile assets  
ENV APP_HOME /var/app  
RUN mkdir -p $APP_HOME  
ADD . $APP_HOME  
WORKDIR $APP_HOME  
RUN RAILS_ENV=production bundle exec rake assets:precompile --trace  
  
CMD ["bin/start_server.sh"]  

