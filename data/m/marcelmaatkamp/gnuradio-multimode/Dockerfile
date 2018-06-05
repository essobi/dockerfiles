FROM marcelmaatkamp/gnuradio  
  
MAINTAINER m.maatkamp@gmail.com version: 0.1  
# ---  
# MultiMode  
ADD gnuradio-multimode /gnuradio/gnuradio-multimode  
RUN cd /gnuradio/gnuradio-multimode && make install  
  
WORKDIR /gnuradio/gnuradio-multimode  
ENTRYPOINT ["/bin/bash"]  

