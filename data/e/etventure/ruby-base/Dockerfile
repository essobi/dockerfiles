FROM ruby:2.3  
RUN apt-get update && apt-get install -y ghostscript \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
  
ADD Gemfile* /opt/app/  
RUN bundle install --binstubs  

