FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=5.3.0  
RUN gem install chef-zero --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["chef-zero"]  
CMD ["--help"]  

