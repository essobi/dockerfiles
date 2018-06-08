FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.16  
RUN gem install cloudhealth-setup --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["cloudhealth-setup"]  
CMD ["--help"]  

