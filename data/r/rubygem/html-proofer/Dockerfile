FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=3.4.0  
RUN gem install html-proofer --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["htmlproofer"]  
CMD ["--help"]  

