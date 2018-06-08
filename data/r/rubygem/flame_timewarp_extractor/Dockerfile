FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=4.0.2  
RUN gem install flame_timewarp_extractor --version ${VERSION} \--no-format-
exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["flametwextract"]  
CMD ["--help"]  

