FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.4.3  
RUN gem install fluent-plugin-secure-forward --version ${VERSION} \--no-
format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["secure-forward-ca-generate"]  
CMD ["--help"]  

