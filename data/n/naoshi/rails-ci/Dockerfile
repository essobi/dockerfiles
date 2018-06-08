#-------------------------------------------------------------------------------  
#  
# WARNING! WARNING! WARNING!  
# THIS IMAGE IS BEING BUILT PUBLICLY  
# DO NOT ADD PRODUCTION SECRETS HERE  
#  
#-------------------------------------------------------------------------------  
FROM naoshi/rails-base:latest  
  
# install apt packages  
RUN apt-get update && apt-get install --no-install-suggests -y \  
qt5-default libqt5webkit5-dev xvfb \  
&& rm -rf /var/lib/apt/lists/*  

