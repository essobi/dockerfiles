FROM ubuntu:trusty  
  
USER root  
  
# Install Dependencies  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y build-essential pkg-config cmake git pigz python-pip
python-dev build-essential && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y  
  
RUN pip install --upgrade pip && \  
pip install --upgrade virtualenv  
  
RUN pip install boutiques  
  
# Get dcm2niix from github and compile  
RUN cd /tmp && \  
git clone https://github.com/rordenlab/dcm2niix.git && \  
cd dcm2niix && mkdir build && cd build && \  
cmake -DBATCH_VERSION=ON -DUSE_OPENJPEG=ON .. && \  
make && make install  
  
RUN git clone https://github.com/neurolabusc/dcm_qa.git /tmp/dcm_qa  
  
ENTRYPOINT ["cd","/tmp"]  

