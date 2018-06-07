# Set up gcc5 for cross-compiling  
  
FROM ubuntu:15.10  
# Copy build scripts  
COPY build/ /build/  
# Ok, so this is one step because it saves a *lot* of disk space, so I'll go
over it here:  
# Install deps:  
# - Source-getting deps  
# - GCC/G++  
# - build dependencies (tools)  
# - build dependencies (libs)  
# Get source/extract source  
# Build  
# Remove deps:  
# (note I leave gcc/g++ installed - this ensures deps for cross-compiler are
avialable)  
# - Source-getting deps  
# - build deps (tools)  
# - build deps (libs)  
# Cleanup unused packages  
# Clean apt cache  
# Remove downloaded lists  
RUN apt-get update && \  
apt-get install -y \  
wget bzip2 \  
gcc g++ \  
make bison flex texinfo \  
libgmp-dev libmpfr-dev libisl-dev libcloog-isl-dev libmpc-dev && \  
/build/get-src.sh && /build/extract-src.sh && \  
/build/build-binutils.sh && /build/build-gcc.sh && \  
rm -rf /build && \  
apt-get purge -y \  
wget bzip2 \  
make bison flex texinfo \  
libgmp-dev libmpfr-dev libisl-dev libcloog-isl-dev libmpc-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

