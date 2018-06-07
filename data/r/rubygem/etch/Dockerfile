FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=5.0.0  
RUN gem install etch --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["etch"]  
CMD ["--help"]  

