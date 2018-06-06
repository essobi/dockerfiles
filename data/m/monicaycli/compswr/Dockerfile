FROM tensorflow/tensorflow:1.7.0-gpu-py3  
  
LABEL maintainer="Monica Li <monica.li@uconn.edu>"  
  
# Directories  
## binds  
RUN mkdir -p /bind/data_in && \  
mkdir -p /bind/data_out && \  
mkdir -p /bind/scripts  
  
# Install python packages  
RUN pip install --upgrade pip  
RUN pip install librosa  
  
# Configuration  
## PREpend user scripts to the path  
ENV PATH /bind/scripts:$PATH  
  
## Other ENVs  
# setup singularity compatible entry points to run the initialization script  
ENTRYPOINT ["/usr/bin/env","/singularity"]  
  
COPY entry_init.sh /singularity  
RUN chmod 755 /singularity  
  
RUN /usr/bin/env \  
| sed '/^HOME/d' \  
| sed '/^HOSTNAME/d' \  
| sed '/^USER/d' \  
| sed '/^PWD/d' > /environment && \  
chmod 755 /environment  

