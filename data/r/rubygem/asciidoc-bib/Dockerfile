FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=2.3.1  
RUN gem install asciidoc-bib --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["asciidoc-bib"]  
CMD ["--help"]  

