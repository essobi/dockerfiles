FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1.2  
RUN gem install gemspec_deps_gen --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gemspec_deps_gen"]  
CMD ["--help"]  

