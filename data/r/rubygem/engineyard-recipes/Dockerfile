FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.5.0  
RUN gem install engineyard-recipes --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["ey-recipes"]  
CMD ["--help"]  

