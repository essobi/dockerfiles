FROM ruby:2.1.7  
ENV PACT_MOCK_SERVICE_VERSION=0.8.0  
RUN gem install pact-mock_service --version $PACT_MOCK_SERVICE_VERSION  
  
RUN mkdir -p /usr/local/pacts  
  
EXPOSE 1234  
ENTRYPOINT ["pact-mock-service", "--pact-specification-version", "2.0.0",
"-l", "/var/log/pact-mock-service.log", "-h", "0.0.0.0", "-d",
"/usr/local/pacts"]  
  
CMD ["-p", "1234"]  
  

