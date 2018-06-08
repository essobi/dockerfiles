FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.8.5  
RUN gem install gaptool-server --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gaptool-server"]  
CMD ["--help"]  

