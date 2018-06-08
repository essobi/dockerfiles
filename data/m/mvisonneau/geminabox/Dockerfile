FROM ruby:2.4.2-alpine3.6  
RUN \  
gem install geminabox ;\  
mkdir -p /opt/geminabox/conf /opt/geminabox/data  
  
ADD /config.ru /opt/geminabox/conf  
  
WORKDIR /opt/geminabox/conf  
  
EXPOSE 9292  
ENTRYPOINT [ "rackup", "--host", "0.0.0.0" ]  

