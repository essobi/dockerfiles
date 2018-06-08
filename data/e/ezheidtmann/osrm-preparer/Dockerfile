FROM ezheidtmann/osrm  
  
ENV OSM_PBF_URL http://download.geofabrik.de/north-america/us/rhode-island-
latest.osm.pbf  
ENV OSRM_FILENAME thedata  
ENV AWS_DESTINATION "s3://osrm-prepared-data/ri.osrm.tar.gz"  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yy install pigz python-pip  
  
RUN pip install awscli  
  
ADD prep.sh prep.sh  
CMD ./prep.sh  

