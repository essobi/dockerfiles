FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.5.0  
RUN gem install gist --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gist"]  
CMD ["--help"]  

