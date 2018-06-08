FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.2.1  
RUN gem install influxdb-lineprotocol-writer --version ${VERSION} \--no-
format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["influxdb-lineprotocol-writer"]  
CMD ["--help"]  

