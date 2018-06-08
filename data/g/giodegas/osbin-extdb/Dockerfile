FROM giodegas/opensim-bin-standalone  
  
MAINTAINER Giovanni De Gasperis <giovanni@giodegas.it>  
  
# useful to upload with scp on OAR file remotely for region backup  
RUN apt-get install -y ssh-client net-tools  
  
ADD StandaloneCommon.ini.extdb /opensim-0.8.0.1/bin/config-
include/StandaloneCommon.ini  
ADD Regions.ini /opensim-0.8.0.1/bin/Regions/Regions.ini  
ADD OpenSim.ini /opensim-0.8.0.1/bin/OpenSim.ini  
  
#External OpenSim ports to accept connections from SL compatible viewers.  
EXPOSE 9001/tcp  
EXPOSE 9001/udp  

