FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.93.6  
RUN gem install giraffesoft-unicorn --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["unicorn"]  
CMD ["--help"]  

