FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.4.1.2  
RUN gem install ezmobius-nanite --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["nanite-agent"]  
CMD ["--help"]  

