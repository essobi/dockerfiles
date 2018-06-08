FROM nginx  
MAINTAINER Gerald Fiedler <gerald@sftech.de>  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /rm -rf /var/lib/apt/lists/*  
  
RUN wget --no-verbose --recursive --no-host-directories --no-parent --convert-
links --directory-prefix=/usr/share/nginx/html \  
http://dds.cr.usgs.gov/srtm/version2_1/SRTM30/  
  

