FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.4.0  
RUN gem install ec2-consistent-snapshot-rb --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ec2-consistent-snapshot-rb"]  
CMD ["--help"]  

