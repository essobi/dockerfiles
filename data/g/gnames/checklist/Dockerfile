FROM ruby:2.2.2-slim  
MAINTAINER Dmitry Mozzherin  
  
ENV LAST_FULL_REBUILD 2015-04-22  
RUN apt-get update -qq && \  
apt-get install -y build-essential libqt4-dev git vim \  
libmysqlclient-dev && \  
mkdir /app  
  
WORKDIR /app  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN bundle install  
  
COPY . /app  
  
CMD ["/app/app.rb"]  

