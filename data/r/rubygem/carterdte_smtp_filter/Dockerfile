FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.6.9  
RUN gem install carterdte_smtp_filter --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["carterdte_smtp_filter"]  
CMD ["--help"]  

