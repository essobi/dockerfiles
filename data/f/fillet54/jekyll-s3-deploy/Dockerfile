FROM ruby:2.2  
  
RUN apt-get update \  
&& apt-get install -y openjdk-7-jre-headless \  
&& apt-get clean  
  
COPY Gemfile /Gemfile  
  
RUN bundle install  

