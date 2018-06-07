FROM ruby:2.3.1  
  
RUN export LANG=en_US.UTF-8  
RUN export LANGUAGE=en_US.UTF-8  
RUN export LC_ALL=en_US.UTF-8  
  
RUN apt-get update && apt-get install openjdk-7-jre ditaa git -y  
  
ADD ./content/Gemfile /src/Gemfile  
  
WORKDIR /src  
  
RUN bundle install  
  
ENTRYPOINT ["/usr/local/bin/bundle","exec","rake"]  
  

