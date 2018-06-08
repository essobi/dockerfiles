FROM guiguem/root-docker:python3  
  
MAINTAINER Mathieu Guigue "Mathieu.Guigue@pnnl.gov"  
COPY . /morpho  
  
RUN /bin/bash -c "source /setup.sh &&\  
pip install /morpho/."  
  
CMD ['source /setup.sh']  

