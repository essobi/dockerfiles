FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.8.6  
RUN gem install fiveruns-dash-sensor --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fiveruns-dash-sensor"]  
CMD ["--help"]  

