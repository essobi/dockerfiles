FROM ruby:2.3  
RUN gem install --no-ri --no-rdoc gemstash  
  
EXPOSE 9292  
CMD ["gemstash", "start", "--no-daemonize"]  

