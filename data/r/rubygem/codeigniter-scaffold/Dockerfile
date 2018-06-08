FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.0  
RUN gem install codeigniter-scaffold --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["codeigniter-scaffold"]  
CMD ["--help"]  

