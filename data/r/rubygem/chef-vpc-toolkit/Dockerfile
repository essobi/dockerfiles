FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.8.2  
RUN gem install chef-vpc-toolkit --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["chef-vpc-toolkit"]  
CMD ["--help"]  

