FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.0.2  
RUN gem install difio-dotcloud-ruby --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["difio-dotcloud"]  
CMD ["--help"]  

