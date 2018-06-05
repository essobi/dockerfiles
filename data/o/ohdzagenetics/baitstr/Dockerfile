# Header  
FROM ubuntu:latest  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
cython \  
gcc \  
python \  
zlibc \  
zlib1g \  
zlib1g-dev  
  
# Pull in source code  
ADD . /src/  
WORKDIR /src/  
  
# Make the install  
RUN make && make install  
  
# Add binaries to PATH  
ENV PATH "$PATH:/src/bin/"  

