###############################################################################  
# Docker Runtime for Meteor Apps with ImageMagick  
# Based on MeteorD (https://github.com/meteorhacks/meteord)  
###############################################################################  
  
# Set the base image to MeteorD  
FROM abernix/meteord:base  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install ImageMagick package  
RUN apt-get install -y imagemagick  

