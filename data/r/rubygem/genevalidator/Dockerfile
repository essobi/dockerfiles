FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=GeneValidator-1.5.2  
RUN gem install genevalidator --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["genevalidator"]  
CMD ["--help"]  

