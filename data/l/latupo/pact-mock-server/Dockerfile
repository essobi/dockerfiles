FROM ruby:2.3.0  
# create workdir  
RUN mkdir -p /var/lib/pact-mock-server  
WORKDIR /var/lib/pact-mock-server  
# copy entrypoint script  
COPY docker-entrypoint.sh /var/lib/pact-mock-server/docker-entrypoint.sh  
ENTRYPOINT ["/var/lib/pact-mock-server/docker-entrypoint.sh"]  
  
# copy Gemfile and run install the pact-mock_service  
COPY ./Gemfile /var/lib/pact-mock-server/Gemfile  
RUN gem install bundler && bundle install  
  
EXPOSE 8000  

