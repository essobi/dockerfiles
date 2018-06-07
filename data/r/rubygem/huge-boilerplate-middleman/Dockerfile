FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.3  
RUN gem install huge-boilerplate-middleman --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["mm-huge"]  
CMD ["--help"]  

