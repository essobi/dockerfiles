FROM fiji/fiji  
  
ENV FIJI=/fiji/fiji-linux64  
ENV MACRO=/NRRDtools/h5j2NRRD.ijm  
  
VOLUME /data  
  
RUN cd / && git clone https://github.com/Robbie1977/NRRDtools.git  
  
RUN apt-get -qq -y update && apt-get -qq -y install xvfb  
  
RUN ./fiji-linux64 --update update  
  
WORKDIR /data/  
  
ENTRYPOINT ["/bin/bash"]  

