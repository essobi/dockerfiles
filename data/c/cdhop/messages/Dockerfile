#Dockerfile  
FROM ruby:2.2.0  
WORKDIR /usr/src/app  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev sqlite3
libsqlite3-dev  
  
COPY Gemfile /usr/src/app/Gemfile  
COPY Gemfile.lock /usr/src/app/Gemfile.lock  
  
RUN bundle install  
  
COPY . /usr/src/app  
# copy our project into the WORKDIR  
EXPOSE 9292  
CMD ["rackup","-o","0.0.0.0"]  
# this is the default command we will run when starting the container*  

