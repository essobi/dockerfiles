FROM ruby  
MAINTAINER think@hotmail.de  
  
RUN gem install gherkin --version=2.12.2 \  
&& gem install gherkin_format --no-format-exec  
  
ENV LC_ALL=C.UTF-8  
ENTRYPOINT ["gherkin_format"]  
CMD ["--help"]  

