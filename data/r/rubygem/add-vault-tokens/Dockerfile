FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.2.6  
RUN gem install add-vault-tokens --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["add-vault-tokens"]  
CMD ["--help"]  

