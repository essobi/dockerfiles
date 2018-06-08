FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.1.4  
RUN gem install git-fogbugz --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["git-fogbugz"]  
CMD ["--help"]  

