FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.82.5  
RUN gem install growthforecast-client --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["growthforecast-client"]  
CMD ["--help"]  

