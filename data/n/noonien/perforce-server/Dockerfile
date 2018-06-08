FROM noonien/perforce-base  
MAINTAINER George Jiglau <george@mux.ro>  
  
# Install the perforce server  
RUN apt-get install -y perforce-server  
  
# Server roots are stored here  
VOLUME /opt/perforce/servers  
  
# Add startup file and run it by default  
COPY run.sh /  
CMD ["/run.sh"]  

