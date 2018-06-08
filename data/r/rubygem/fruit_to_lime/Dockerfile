FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.7.1  
RUN gem install fruit_to_lime --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fruit_to_lime"]  
CMD ["--help"]  

