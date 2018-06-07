FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.3.2  
RUN gem install executable-hooks --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["executable-hooks-uninstaller"]  
CMD ["--help"]  

