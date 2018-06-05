FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.5.4.4  
RUN gem install benhoskings-ambition --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ambition_adapter"]  
CMD ["--help"]  

