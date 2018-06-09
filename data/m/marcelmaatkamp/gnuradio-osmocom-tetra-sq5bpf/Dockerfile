FROM marcelmaatkamp/gnuradio-libosmocore-sq5bpf  
  
MAINTAINER m.maatkamp@gmail.com version: 0.1  
# ---  
# Tetra  
ADD src /gnuradio/osmocom/osmo-tetra-sq5bpf  
  
RUN cd /gnuradio/osmocom/osmo-tetra-sq5bpf && make  
  
ENTRYPOINT ["/bin/bash"]  

