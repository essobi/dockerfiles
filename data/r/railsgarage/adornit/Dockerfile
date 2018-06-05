FROM instructure/ruby-passenger:2.3  
USER root  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
  
RUN bundle install --jobs 4  
  
COPY . /usr/src/app  
  
RUN chown -R docker:docker /usr/src/app  
RUN chown -R docker:docker /home/docker  
USER docker  

