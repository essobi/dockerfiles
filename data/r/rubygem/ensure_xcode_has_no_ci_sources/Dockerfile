FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1.2  
RUN gem install ensure_xcode_has_no_ci_sources --version ${VERSION} \--no-
format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ensure_xcode_has_no_ci_sources"]  
CMD ["--help"]  

