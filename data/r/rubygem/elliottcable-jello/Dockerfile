FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=7  
RUN gem install elliottcable-jello --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["jello"]  
CMD ["--help"]  

