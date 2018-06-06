FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.1.9  
RUN gem install capistrano-extensions --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["capistrano-extensions-sync-content"]  
CMD ["--help"]  

