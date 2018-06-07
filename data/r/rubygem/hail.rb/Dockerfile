FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2016.01.19.01.22  
RUN gem install hail.rb --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["hail"]  
CMD ["--help"]  

