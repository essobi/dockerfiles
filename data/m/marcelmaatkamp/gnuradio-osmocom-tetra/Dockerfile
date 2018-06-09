FROM marcelmaatkamp/gnuradio-libosmocore  
  
MAINTAINER m.maatkamp@gmail.com version: 0.1  
# ---  
# Tetra  
ADD src/ /gnuradio/osmo-tetra/src  
RUN cd /gnuradio/osmo-tetra/src && make  
  
ENTRYPOINT ["/bin/bash"]  

