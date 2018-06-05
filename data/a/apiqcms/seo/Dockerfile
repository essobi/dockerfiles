FROM ruby:alpine  
MAINTAINER Igor Petrov <garik.piton@gmail.com>  
ENV INSTALL_PATH /kms  
# Set Rails to run in production  
ENV RAILS_ENV production  
  
RUN apk update && apk --update --no-cache add libstdc++ postgresql-client
tzdata && mkdir $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY Gemfile Gemfile  
  
RUN apk --update --no-cache add --virtual build-deps build-base python
postgresql-dev nodejs g++; \  
bundle install --without development test && apk del build-deps  
  
COPY . .  
  
EXPOSE 3000  
# Expose a volume so that nginx will be able to read in assets in production.  
VOLUME ["$INSTALL_PATH/public"]  
  
# Configure an entry point, so we don't need to specify  
# "bundle exec" for each of our commands.  
ENTRYPOINT ["bundle", "exec"]  
  
CMD ["rails", "server", "-b", "0.0.0.0"]  

