FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=5.0.2  
RUN gem install govspeak --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["govspeak"]  
CMD ["--help"]  

