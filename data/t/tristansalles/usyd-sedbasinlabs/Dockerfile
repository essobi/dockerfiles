FROM tristansalles/usyd-uos-geos-base:v1.01  
MAINTAINER Tristan Salles  
  
# Get debian base install and some unnecessary files, copy local data to
workspace  
RUN mkdir /workspace && \  
mkdir /workspace/volume  
  
# Copy local directory to image  
COPY UoS /workspace  
  
# expose notebook port  
EXPOSE 8888  
# setup space for working in  
VOLUME /workspace/volume  
  
# launch notebook  
WORKDIR /workspace  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
CMD jupyter notebook --ip=0.0.0.0 --no-browser \  
\--NotebookApp.default_url='/tree/StartHere.ipynb'  

