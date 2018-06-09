FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.0.0.pre.111215  
RUN gem install erichummel-sunspot --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["sunspot-solr"]  
CMD ["--help"]  

