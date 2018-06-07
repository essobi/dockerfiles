FROM ruby:2.1.5  
MAINTAINER Miguel Palhas <mpalhas@groupbuddies.com>  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y postgresql-client libqt4-dev
libqtwebkit-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1 \  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
EXPOSE 3000  
CMD ["bundle", "exec", "foreman", "start"]  

