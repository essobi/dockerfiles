FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.1.4.3  
RUN gem install cluster-fuck --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["clusterfuck"]  
CMD ["--help"]  

