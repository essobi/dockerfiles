FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=20121026.1  
RUN gem install abiquo-installer-tests --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["abiquo-installer-tests"]  
CMD ["--help"]  

