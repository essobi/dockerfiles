FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.7.16  
RUN gem install giraffesoft-chef --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["chef-client"]  
CMD ["--help"]  

