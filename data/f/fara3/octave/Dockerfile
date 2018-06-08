# Use latest debain wheezy image as the base  
FROM debian:wheezy  
MAINTAINER Ramón Díez Lejarazu (ramon.diez.lejarazu@gmail.com)  
  
# Install dev tools to compile  
RUN apt-get update && apt-get install -y \  
octave \  
less  
  
# House cleaning  
RUN apt-get autoclean  
  
#Set up the working directory  
WORKDIR /projects  
  
#Run octave shell  
CMD ["octave"]  

