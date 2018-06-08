FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1b  
  
RUN gem install jruby-slick --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["jruby-slick.rb"]  
CMD ["--help"]  

