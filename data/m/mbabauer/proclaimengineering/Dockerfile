FROM meteorhacks/meteord:base  
  
# Install GraphicsMagick and ImageMagick  
RUN apt-get update  
RUN apt-get -y install graphicsmagick imagemagick  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*d  

