FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.1.0  
RUN gem install gemma --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gemma"]  
CMD ["--help"]  

