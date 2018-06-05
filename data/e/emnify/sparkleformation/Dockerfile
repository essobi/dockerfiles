FROM ruby:2.4-stretch  
ARG version=3.0.28  
RUN gem install sfn -v $version  
  
VOLUME /work  
WORKDIR /work  
ENTRYPOINT ["/usr/local/bundle/bin/sfn"]  

