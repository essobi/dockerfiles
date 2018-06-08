FROM scrapybook/base  
  
# Auto-start web server  
RUN mkdir /etc/service/bookweb  
COPY start.sh /etc/service/bookweb/run  
  
# Copy web server's image  
COPY app /opt/app  
  
EXPOSE 9312  

