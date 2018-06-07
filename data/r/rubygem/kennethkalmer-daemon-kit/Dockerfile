FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.1.7.9  
RUN gem install kennethkalmer-daemon-kit --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["daemon_kit"]  
CMD ["--help"]  

