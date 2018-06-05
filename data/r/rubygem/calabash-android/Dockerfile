FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.9.1.pre1  
  
RUN gem install calabash-android --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["calabash-android"]  
CMD ["--help"]  

