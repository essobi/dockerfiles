FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.7  
RUN gem install bitcoin-cigs --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["bitcoin-cigs"]  
CMD ["--help"]  

