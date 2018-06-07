FROM kmallea/steamcmd  
MAINTAINER Jacob Tomlinson <jacob@tom.linson.uk>  
  
# Create insurgency directory  
RUN mkdir /opt/insurgency  
  
# Add startup script  
ADD startup.sh /usr/src/app/startup.sh  
RUN chmod +x /usr/src/app/startup.sh  
  
# Make server port available to host  
EXPOSE 27015  
WORKDIR /opt/insurgency  
  
# Update and run insurgency  
ENTRYPOINT ["/usr/src/app/startup.sh"]  
  
# Run in insurgency in console mode  
CMD ["updaterun", "-console"]  

