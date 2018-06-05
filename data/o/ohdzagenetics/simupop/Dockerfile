# Header  
FROM continuumio/miniconda3  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
gcc \  
g++ \  
libz-dev \  
libbz2-dev \  
swig  
  
# Copy in source code  
COPY . /src/  
  
# Set WORKDIR to source code  
WORKDIR /src/  
  
# Install the software  
RUN python3 setup.py install  
  

