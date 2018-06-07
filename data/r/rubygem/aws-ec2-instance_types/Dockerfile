FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.4.1  
RUN gem install aws-ec2-instance_types --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["aws-ec2-instance_types"]  
CMD ["--help"]  

