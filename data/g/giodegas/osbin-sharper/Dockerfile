FROM giodegas/osbin-extdb  
  
MAINTAINER Giovanni De Gasperis <giovanni@giodegas.it>  
  
ADD Regions.ini.Sharper /opensim-0.8.0.1/bin/Regions/Regions.ini  
ADD OpenSim.ini.CS.Sharper /opensim-0.8.0.1/bin/OpenSim.ini  
ADD SharperLand260914.oar /opensim-0.8.0.1/bin/  
  
#External OpenSim ports to accept connections from SL compatible viewers.  
EXPOSE 9001/tcp  
EXPOSE 9001/udp  

