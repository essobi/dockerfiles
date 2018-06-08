FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.1.5  
RUN gem install fingerprint --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fingerprint"]  
CMD ["--help"]  

