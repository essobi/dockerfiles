FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1.3  
RUN gem install blinky-tape-test-status --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["blinky-tape-test-tool"]  
CMD ["--help"]  

