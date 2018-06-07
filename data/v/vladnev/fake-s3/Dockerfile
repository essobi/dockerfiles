FROM ruby:2.5-slim  
  
RUN gem install fakes3 -v 0.2.5  
  
RUN mkdir /storage  
  
ENTRYPOINT ["fakes3"]  
CMD ["-r", "/storage", "-p", "9000", "-H", "localhost"]  

