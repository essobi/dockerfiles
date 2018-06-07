FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.18.8  
RUN gem install ajmalafif-jumpstart --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["jumpstart"]  
CMD ["--help"]  

