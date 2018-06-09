FROM ruby:2.1  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY ./ssh /root/.ssh/  
  
COPY Gemfile /app  
COPY Gemfile.lock /app  
RUN bundle install --jobs 3  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 net-tools --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
COPY . /app  
  
CMD ["puma", "-C", "config/puma.rb"]  

