FROM ruby:2.3  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install sqlite3 --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
RUN bundle install  

