FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=5.0.0  
RUN gem install egads --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["egads"]  
CMD ["--help"]  

