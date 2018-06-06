FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.3.1  
RUN gem install capistrano_deploy_lock --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["cap_deploy_lock_msg"]  
CMD ["--help"]  

