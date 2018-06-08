FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.2.1  
RUN gem install freshbooks --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["freshbooks"]  
CMD ["--help"]  

