FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1.7  
RUN gem install forward --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["forward"]  
CMD ["--help"]  

