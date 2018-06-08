FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=9.0.0  
RUN gem install foodcritic --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["foodcritic"]  
CMD ["--help"]  

