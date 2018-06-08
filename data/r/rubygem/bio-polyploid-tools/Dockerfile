FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.7.3  
RUN gem install bio-polyploid-tools --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["bfr.rb"]  
CMD ["--help"]  

