FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.9.0.rc2  
  
RUN gem install invo-sporknife --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["sporknife"]  
CMD ["--help"]  

