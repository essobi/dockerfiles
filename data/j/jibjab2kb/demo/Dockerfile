FROM ruby:2.2.0  
RUN apt-get update -qq && apt-get install -y build-essential nodejs npm
nodejs-legacy mysql-client  
RUN npm install -g phantomjs  
  
RUN mkdir -p /code/demo  
  
WORKDIR /tmp  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN bundle install  
  
ADD . /code/demo  
WORKDIR /code/demo  
CMD ["rails","server","-b","0.0.0.0"]  
  
EXPOSE 3000  

