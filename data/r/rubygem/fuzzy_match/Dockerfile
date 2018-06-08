FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.1.0  
RUN gem install fuzzy_match --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fuzzy_match"]  
CMD ["--help"]  

