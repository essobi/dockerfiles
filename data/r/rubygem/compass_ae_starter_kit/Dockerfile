FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.2.0  
RUN gem install compass_ae_starter_kit --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["compass_ae"]  
CMD ["--help"]  

