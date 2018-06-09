FROM ruby:2.3  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY Gemfile /app  
COPY Gemfile.lock /app  
RUN bundle install --jobs 5  
  
COPY . /app  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
CMD ["rails", "server", "-b", "0.0.0.0"]  

