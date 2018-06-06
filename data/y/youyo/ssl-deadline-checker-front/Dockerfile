FROM ruby:2.4-alpine  
MAINTAINER youyo  
  
ENV APP_DIR /app  
  
ADD . ${APP_DIR}  
WORKDIR ${APP_DIR}  
RUN bundle install  
  
EXPOSE 4567:4567  
ENTRYPOINT ["bundle","exec","ruby","app.rb"]  

