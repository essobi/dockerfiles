FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.4.9.diaspora.0.1.22  
RUN gem install diaspora-vines --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["vines"]  
CMD ["--help"]  

