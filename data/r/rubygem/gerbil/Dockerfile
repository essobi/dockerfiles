FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=3.1.0  
RUN gem install gerbil --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gerbil"]  
CMD ["--help"]  

