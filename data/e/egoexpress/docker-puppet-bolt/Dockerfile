FROM ruby:2.5  
  
RUN gem install bolt -v 0.19.0  
  
RUN groupadd -r bolt && useradd --no-log-init -r -g bolt bolt  
  
USER bolt:bolt  
ENTRYPOINT ["bolt"]  
CMD ["--help"]  

