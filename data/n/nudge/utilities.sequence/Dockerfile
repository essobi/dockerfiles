#Dockerfile  
FROM ruby:2.2.0  
WORKDIR /usr/src/app/  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev  
  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" && chmod +x /usr/local/bin/gosu  
  
COPY Gemfile /usr/src/app/Gemfile  
COPY Gemfile.lock /usr/src/app/Gemfile.lock  
  
RUN bundle install  
  
COPY . /usr/src/app  
# copy our project into the WORKDIR  
EXPOSE 3000  
CMD ["rails", "server","-b","0.0.0.0"]  
# this is the default command we will run when starting the container*  

