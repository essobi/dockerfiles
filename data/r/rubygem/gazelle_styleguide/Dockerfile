FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.0.8  
RUN gem install gazelle_styleguide --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["gazelle_styleguide"]  
CMD ["--help"]  

