FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.7  
RUN gem install gherkin_format --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gherkin_format"]  
CMD ["--help"]  

