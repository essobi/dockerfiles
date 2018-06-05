FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.2.8  
RUN gem install brianjlandau-acts_as_archive --version ${VERSION} \--no-
format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["acts_as_archive"]  
CMD ["--help"]  

