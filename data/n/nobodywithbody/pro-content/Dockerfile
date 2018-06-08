FROM ruby:latest  
WORKDIR /www/app  
ADD . .  
RUN gem install bundler puma foreman  
RUN bundler install  
EXPOSE 80  

