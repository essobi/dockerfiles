FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.1.0.beta1  
  
RUN gem install github-nippou --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["github-nippou"]  
CMD ["--help"]  

