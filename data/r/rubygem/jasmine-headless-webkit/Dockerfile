FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.9.0.rc.2  
RUN gem install jasmine-headless-webkit --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["jasmine-headless-webkit"]  
CMD ["--help"]  

