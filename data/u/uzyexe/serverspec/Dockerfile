FROM ruby:2.4.2  
ENV SERVERSPEC_VERSION 2.41.0  
ENV RUBOCOP_VERSION 0.50.0  
RUN gem install serverspec -v ${SERVERSPEC_VERSION} && \  
gem install rubocop -v ${RUBOCOP_VERSION}  
  
WORKDIR /serverspec  
  
ENTRYPOINT ["/usr/local/bin/rake"]  
CMD ["--tasks"]  

