FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.5.0.alpha  
  
RUN gem install jruby-hornetq --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["hornetq_server"]  
CMD ["--help"]  

