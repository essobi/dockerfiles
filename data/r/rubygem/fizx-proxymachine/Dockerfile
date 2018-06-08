FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.8.0  
RUN gem install fizx-proxymachine --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["proxymachine"]  
CMD ["--help"]  

