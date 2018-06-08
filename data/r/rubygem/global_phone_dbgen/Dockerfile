FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.0.0  
RUN gem install global_phone_dbgen --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["global_phone_dbgen"]  
CMD ["--help"]  

