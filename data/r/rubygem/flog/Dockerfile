FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.6.1  
RUN gem install flog --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["flog"]  
CMD ["--help"]  

