FROM ubuntu:14.04  
USER root  
RUN apt-get update && apt-get install -y wget iptables libfontconfig  
ADD start_phantomjs_with_content_blocking.sh
/opt/start_phantomjs_with_content_blocking.sh  
  
ADD https://s3.amazonaws.com/wiser.phantomjs/phantomjs
/usr/local/bin/phantomjs  
RUN chmod +x /usr/local/bin/phantomjs  
  
RUN chmod 755 /opt/start_phantomjs_with_content_blocking.sh  
  
EXPOSE 8910  
CMD /opt/start_phantomjs_with_content_blocking.sh  
  
# CMD /usr/local/bin/phantomjs --webdriver 8910  

