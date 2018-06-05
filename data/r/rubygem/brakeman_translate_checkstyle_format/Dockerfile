FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.1  
RUN gem install brakeman_translate_checkstyle_format --version ${VERSION}
\--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["brakeman_translate_checkstyle_format"]  
CMD ["--help"]  

