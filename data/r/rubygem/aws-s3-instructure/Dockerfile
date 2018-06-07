FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.6.2.1352914936  
RUN gem install aws-s3-instructure --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["s3sh"]  
CMD ["--help"]  

