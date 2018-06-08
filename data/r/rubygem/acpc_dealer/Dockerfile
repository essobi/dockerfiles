FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=3.1.0  
RUN gem install acpc_dealer --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["acpc_dealer"]  
CMD ["--help"]  

