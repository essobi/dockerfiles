FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.0.2  
RUN gem install github-markdown-preview --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["github-markdown-preview"]  
CMD ["--help"]  

