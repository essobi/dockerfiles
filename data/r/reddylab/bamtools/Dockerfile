FROM phusion/baseimage  
MAINTAINER Alejandro Barrera <alejandro.barrera@duke.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
curl \  
unzip \  
cmake \  
g++ \  
zlib1g-dev  
  
# Define env variables for download  
ENV BAMTOOLS_URL=https://github.com/pezmaster31/bamtools/archive/  
ENV BAMTOOLS_RELEASE=2.2.3  
ENV DEST_DIR=/opt  
  
# Download BAMTOOLS, unzip, compile and install it, removing unnecessary files
afterwards  
RUN curl -SLo ${DEST_DIR}/BAMTOOLS-${BAMTOOLS_RELEASE}.zip
${BAMTOOLS_URL}/v${BAMTOOLS_RELEASE}.zip && \  
unzip ${DEST_DIR}/BAMTOOLS-${BAMTOOLS_RELEASE}.zip -d ${DEST_DIR} && \  
rm ${DEST_DIR}/BAMTOOLS-${BAMTOOLS_RELEASE}.zip && \  
cd ${DEST_DIR}/bamtools-${BAMTOOLS_RELEASE} && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install && \  
cp ${DEST_DIR}/bamtools-${BAMTOOLS_RELEASE}/lib/* /lib/ && \  
rm -rf ${DEST_DIR}/BAMTOOLS-${BAMTOOLS_RELEASE}  
  
CMD ["bamtools"]  

