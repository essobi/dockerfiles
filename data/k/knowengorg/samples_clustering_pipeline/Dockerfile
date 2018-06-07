FROM knowengdev/base_image:09_19_2017  
LABEL Xi Chen="xichen24@illinois.edu" \  
Jing Ge="jingge2@illinois.edu" \  
Dan Lanier="lanier4@illinois.edu" \  
Nahil Sobh="sobh@illinois.edu"  
  
ENV SRC_LOC /home  
  
# Install the latest knpackage  
RUN pip3 install -I knpackage dispy  
  
# Clone from github  
RUN git clone https://github.com/KnowEnG/Samples_Clustering_Pipeline.git
${SRC_LOC}  
  
# Set up working directory  
WORKDIR ${SRC_LOC}  

