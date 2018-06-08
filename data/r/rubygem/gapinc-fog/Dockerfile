FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.14.0  
RUN gem install gapinc-fog --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fog"]  
CMD ["--help"]  

