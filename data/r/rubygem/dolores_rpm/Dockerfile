FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=3.3.4.fork  
  
RUN gem install dolores_rpm --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["newrelic_cmd"]  
CMD ["--help"]  

