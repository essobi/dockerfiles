FROM debian  
  
RUN apt-get update -y  
RUN apt-get -y install wkhtmltopdf-dbg  
RUN apt-get -y install xvfb  
RUN apt-get -y install libxrender1 libfontconfig1 libssl-dev  
  
RUN chmod 755 /usr/bin/wkhtmltopdf  
RUN chmod 755 /usr/bin/wkhtmltoimage  
  
# Add start script  
ADD start.sh /usr/bin/start.sh  
RUN chmod 755 /usr/bin/start.sh  
  
# Execute start script to keep container running  
CMD [ "/usr/bin/start.sh" ]  

