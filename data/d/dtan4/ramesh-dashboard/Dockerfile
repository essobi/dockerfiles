FROM ruby:2.2.0  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install --without test development --system  
  
COPY . /usr/src/app  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
  
EXPOSE 5000  
ENTRYPOINT ["bin/docker-entrypoint.sh"]  

