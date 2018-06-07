FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=9001  
RUN gem install bofh-excuse --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["bofh-excuse"]  
CMD ["--help"]  

