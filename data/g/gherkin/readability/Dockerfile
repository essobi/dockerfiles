FROM ruby  
MAINTAINER think@hotmail.de  
  
RUN \  
gem install gherkin_readability --no-format-exec  
  
ENV LC_ALL=C.UTF-8  
ENTRYPOINT ["gherkin_readability"]  
CMD ["--help"]  

