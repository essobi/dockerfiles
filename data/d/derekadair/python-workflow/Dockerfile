FROM derekadair/python-workflow:onbuild  
MAINTAINER Derek Adair "d@derekadair.com"  
# Add packages for firefox to list  
RUN echo "deb http://packages.linuxmint.com debian import" >>
/etc/apt/sources.list  
  
RUN apt-get update -y && \  
apt-get install --force-yes -y \  
# Install fonts + firefox for headless testing in selenium  
xvfb \  
firefox \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic  
  
# cleanup  
RUN apt-get clean  

