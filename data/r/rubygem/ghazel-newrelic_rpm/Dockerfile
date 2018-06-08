FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=3.4.0.2  
RUN gem install ghazel-newrelic_rpm --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["mongrel_rpm"]  
CMD ["--help"]  

