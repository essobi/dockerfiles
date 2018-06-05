FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=9.9.0  
RUN gem install bookbindery --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["bookbinder"]  
CMD ["--help"]  

