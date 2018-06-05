FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=9.0.6  
RUN gem install byebug --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["byebug"]  
CMD ["--help"]  

