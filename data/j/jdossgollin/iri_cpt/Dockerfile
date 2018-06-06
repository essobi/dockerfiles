FROM ubuntu:17.10  
  
RUN apt-get -y update && apt-get -y upgrade &&\  
apt-get -y install build-essential &&\  
apt-get -y install gfortran &&\  
apt-get -y install wget &&\  
wget \--no-check-certificate
https://iri.columbia.edu/climate/tools/cpt/source/CPT.15.5.12.tar.gz &&\  
tar xvzf CPT.15.5.12.tar.gz &&\  
cd CPT/15.5.12 &&\  
make  
  
CMD /bin/bash -c "cd /CPT/15.5.12 && ./CPT.x"

