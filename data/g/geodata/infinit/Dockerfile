##  
# geodata/infinit  
#  
# Executables for the Infinit Storage Platform <https://infinit.sh/>.  
#  
FROM ubuntu:14.04  
MAINTAINER Homme Zwaagstra <hrz@geodata.soton.ac.uk>  
  
# Install the application.  
ADD . /tmp/build/  
RUN /tmp/build/build.sh  
  
# Add the infinit executables to the PATH.  
ENV PATH="/opt/infinit/bin:${PATH}"  

