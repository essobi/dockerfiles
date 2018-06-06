FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.0.1  
RUN gem install aws-cleaner --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["aws_cleaner.rb"]  
CMD ["--help"]  

