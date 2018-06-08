FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.0.9  
RUN gem install Floppy-amee --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ameesh"]  
CMD ["--help"]  

