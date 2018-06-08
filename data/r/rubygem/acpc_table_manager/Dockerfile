FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.0.1  
RUN gem install acpc_table_manager --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["acpc_proxy"]  
CMD ["--help"]  

