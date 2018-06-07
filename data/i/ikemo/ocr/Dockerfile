FROM ruby:2.5  
  
RUN gem install google-cloud-vision  
RUN mkdir /opt/script  
COPY ocr.rb /opt/script/ocr.rb  
ENTRYPOINT ["/opt/script/entrypoint.sh"]  

