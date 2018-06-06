###########################################################  
#  
# Base image with Node.js, unoconv and imagemagick  
#  
###########################################################  
  
FROM node:4  
  
# copy Microsoft Windows Fonts to /usr/share/fonts/WindowsFonts  
ADD WindowsFonts /usr/share/fonts/WindowsFonts  
RUN fc-cache  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git unoconv imagemagick
ghostscript && apt-get clean  
  
RUN /usr/bin/unoconv --listener &  

