FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1.1  
RUN gem install bundler-reorganizer --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["bundler-reorganizer"]  
CMD ["--help"]  

