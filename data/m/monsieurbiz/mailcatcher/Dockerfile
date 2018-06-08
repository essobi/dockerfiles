FROM helder/ruby:2.2  
LABEL maintainer "Monsieur Biz <docker@monsieurbiz.com>"  
  
RUN gem install mailcatcher --no-rdoc --no-ri  
  
EXPOSE 25 1080  
CMD ["mailcatcher", "--smtp-ip=0.0.0.0", "--smtp-port=25", "--http-
ip=0.0.0.0", "--http-port=1080", "-f"]  
  

