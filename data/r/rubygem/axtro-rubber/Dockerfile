FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.5.7.1  
RUN gem install axtro-rubber --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["vulcanize"]  
CMD ["--help"]  

