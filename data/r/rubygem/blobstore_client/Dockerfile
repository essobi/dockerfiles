FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.5.0.pre.1657  
RUN gem install blobstore_client --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["blobstore_client_console"]  
CMD ["--help"]  

