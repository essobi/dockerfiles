FROM ruby:2.3  
MAINTAINER Stanko Krtalic Rusendic <stanko.krtalic@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install slanger  
COPY . .  
  
EXPOSE 4567 8080  
CMD "./start.sh"  

