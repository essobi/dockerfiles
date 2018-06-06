FROM ruby:alpine  
RUN mkdir /puppet  
WORKDIR /puppet  
RUN gem install puppet-lint  
RUN gem install rspec-puppet  
RUN gem install puppet  
COPY bootstrap.sh /puppet  
ENTRYPOINT ["/puppet/bootstrap.sh"]  

