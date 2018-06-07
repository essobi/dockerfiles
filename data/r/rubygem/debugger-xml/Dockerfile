FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.5.0.pre2  
  
RUN gem install debugger-xml --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["rdebug-ide"]  
CMD ["--help"]  

