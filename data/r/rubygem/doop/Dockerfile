FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.5.2  
RUN gem install doop --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT [".gitignore"]  
CMD ["--help"]  

