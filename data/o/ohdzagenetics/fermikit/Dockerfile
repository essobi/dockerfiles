# Header  
FROM ubuntu:latest  
  
# Update package cache  
RUN apt-get update  
  
# Install dependencies)  
RUn apt-get update && apt-get install -y \  
build-essential \  
git \  
zlib1g-dev  
  
# Pull in source code  
COPY . /src  
  
# Test the install  
WORKDIR /src  
  
# Build  
RUN make  
  
# Add new commands to PATH  
ENV PATH "/src/fermi.kit/:$PATH"  
# Test the install, references binaries made during make  
RUN test/test.sh  
  

