FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.1.0  
RUN gem install checkstyle_filter-git --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["checkstyle_filter-git"]  
CMD ["--help"]  

