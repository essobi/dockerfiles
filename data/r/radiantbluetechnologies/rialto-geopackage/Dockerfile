# radiantbluetechnologies/rialto-geopackage  
FROM radiantbluetechnologies/rialtobase-centos  
  
MAINTAINER mpg@flaxen.com  
  
ENV OSSIM_DEV_HOME=/tmp/sources/ossim \  
OSSIM_BUILD_DIR=/tmp/builds/ossim \  
OSSIM_DEPENDENCIES=/usr \  
OSSIM_PREFS_FILE=/usr/share/ossim/ossim_preferences \  
OSSIM_INSTALL_PREFIX=/usr \  
OSSIM_DATA=/usr/share/ossim \  
RIALTO_BRANCH=dev  
  
COPY ./build.sh /tmp/  
RUN /tmp/build.sh  
  
CMD /bin/bash  

