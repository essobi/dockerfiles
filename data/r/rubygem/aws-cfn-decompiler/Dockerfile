FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.9.6  
RUN gem install aws-cfn-decompiler --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["cfn-decompiler"]  
CMD ["--help"]  

