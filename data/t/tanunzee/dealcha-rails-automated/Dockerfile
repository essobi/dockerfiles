FROM tanunzee/dealcha-base:latest  
  
#RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
#RUN apt-get update && apt-get install -y mysql-client sqlite3 --no-install-
recommends && rm -rf /var/lib/apt/lists/*  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
# RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD ["/bin/sh", "start_server.sh"]

