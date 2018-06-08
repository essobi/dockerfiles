FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.9.0  
RUN gem install forking_test_runner --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["forking-test-runner"]  
CMD ["--help"]  

