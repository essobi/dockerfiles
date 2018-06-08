FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.7.0  
RUN gem install ec2-rotate-volume-snapshots --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ec2-rotate-volume-snapshots"]  
CMD ["--help"]  

