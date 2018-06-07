FROM instantci/instantci-docker-ruby:ruby-2.3.0  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN bundle config --global frozen 1  
  
RUN gem install foreman  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY Gemfile /usr/src/app/  
ONBUILD COPY Gemfile.lock /usr/src/app/  
ONBUILD RUN bundle install  
ONBUILD COPY . /usr/src/app  
  
EXPOSE 3000  
CMD ["foreman", "start"]  

