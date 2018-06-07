FROM ruby:2.2-alpine  
  
RUN apk add --no-cache build-base  
  
WORKDIR /opt/fakepusher  
  
COPY Gemfile /opt/fakepusher/Gemfile  
RUN bundle install  
  
COPY . /opt/fakepusher/  
  
EXPOSE 4550 4551  
CMD ["/opt/fakepusher/bin/fakepusher"]  

