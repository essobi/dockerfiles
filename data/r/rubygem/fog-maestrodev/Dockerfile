FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.8.0.20130114204828  
RUN gem install fog-maestrodev --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fog"]  
CMD ["--help"]  

