FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.3.0  
RUN gem install getting_dumped --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["getting_dumped_server"]  
CMD ["--help"]  

