FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=0.1.6  
RUN gem install conan_deploy_stackato3 --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["conan-stackato3"]  
CMD ["--help"]  

