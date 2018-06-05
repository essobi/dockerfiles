FROM ruby:2-slim-stretch  
  
MAINTAINER Dariusz Gafka <d.gafka@madkom.pl>  
  
ENV GEM_HOME "/opt/gems"  
ENV GEM_PATH "/opt"  
ENV PACT_MOCK_SERVICE "0.7.2"  
RUN mkdir /opt/gems && \  
gem install pact-mock_service -v $PACT_MOCK_SERVICE && \  
ln -s /opt/gems/gems/pact-mock_service-$PACT_MOCK_SERVICE/bin/pact-mock-
service /usr/local/bin && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 1234  
VOLUME ["/var/log/pacto", "/opt/contracts"];  
  
ENTRYPOINT ["pact-mock-service", "--pact-specification-version", "2.0.0",
"-l", "/var/log/pacto/pact-mock-service.log", "-h", "0.0.0.0", "-d",
"/opt/contracts"]  
  
CMD ["-p", "1234"]  

