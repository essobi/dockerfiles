FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.7.3  
RUN gem install gitscape --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gitscape"]  
CMD ["--help"]  

