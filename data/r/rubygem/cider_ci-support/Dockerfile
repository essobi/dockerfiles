FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=3.2.0  
RUN gem install cider_ci-support --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["cider-ci_flay"]  
CMD ["--help"]  

