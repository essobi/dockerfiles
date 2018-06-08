FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=3.2.13  
RUN gem install aliddle-sass --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["sass"]  
CMD ["--help"]  

