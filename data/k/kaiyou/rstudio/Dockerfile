FROM rocker/rstudio  
  
COPY rserver.conf /etc/rstudio/rserver.conf  
COPY start.sh /start.sh  
  
RUN chmod u+s `which rserver` `which chown` \  
&& cp /usr/local/lib/R/lib/*.so /usr/lib/  
  
USER rstudio-server  
  
CMD ["/start.sh"]  

