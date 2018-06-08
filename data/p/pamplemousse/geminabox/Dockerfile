FROM ruby:alpine  
  
RUN gem install geminabox  
RUN mkdir /geminabox /geminabox/data  
  
COPY config.ru /geminabox/config.ru  
  
WORKDIR /geminabox  
EXPOSE 9292  
ENTRYPOINT ["rackup", "--host", "0.0.0.0"]  

