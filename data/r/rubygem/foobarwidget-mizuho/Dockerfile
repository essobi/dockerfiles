FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.9.5  
RUN gem install FooBarWidget-mizuho --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["mizuho"]  
CMD ["--help"]  

