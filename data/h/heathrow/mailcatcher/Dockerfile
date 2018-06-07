FROM ruby:2.2  
RUN gem install mailcatcher --no-rdoc --no-ri  
  
EXPOSE 25  
EXPOSE 80  
ENTRYPOINT ["mailcatcher", "--smtp-ip=0.0.0.0", "--smtp-port=25", "--http-
ip=0.0.0.0", "--http-port=80", "--foreground"]  

