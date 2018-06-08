FROM ruby:2.3.1  
MAINTAINER MJ "tywf91@gmail.com"  
RUN apt-get update  
RUN apt-get install nginx -y  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN apt-get install -y build-essential  
  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
RUN gem install foreman

