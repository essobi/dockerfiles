FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.1.7  
RUN gem install ec2-snapshot-replicator --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ec2-snapshot-replicator"]  
CMD ["--help"]  

