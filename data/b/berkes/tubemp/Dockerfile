# Taken from https://github.com/docker-
library/ruby/blob/069e9f5f9aa4903f4a3cb4baf6325d08d9d366e6/1.9/onbuild/Dockerfile  
# We don't use ruby:1.9-onbuilt because that tries to `gem install` before
we've had a chance to install rmagick dependencies.  
FROM ruby:1.9.3-p551  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
# Create the dir where our app is going to live  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install imagemagick dependencies for rmagick gem.  
RUN ["apt-get", "update", "-qq"]  
RUN ["apt-get", "install", "-y", "build-essential", "imagemagick",
"libmagickcore-dev", "libmagickwand-dev"]  
  
# Install bundle  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
# Place the app on the container  
COPY . /usr/src/app  
  
EXPOSE 8080  
ENV RACK_ENV production  
ENTRYPOINT unicorn --port 8080 --env $RACK_ENV config.ru  
CMD []  

