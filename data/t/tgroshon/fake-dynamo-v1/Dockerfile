FROM ruby:2.1  
RUN gem install fake_dynamo --version 0.1.3  
  
EXPOSE 3000  
ENTRYPOINT ["/usr/local/bundle/bin/fake_dynamo"]  
  
CMD ["-p", "3000"]

