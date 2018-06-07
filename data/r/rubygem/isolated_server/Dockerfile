FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.4.9  
RUN gem install isolated_server --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["boot_isolated_mysql_server"]  
CMD ["--help"]  

