FROM phusion/baseimage  
MAINTAINER Alejandro Barrera <alejandro.barrera@duke.edu>  
  
# Install dependencies  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
zlib1g-dev \  
python  
  
# Installs bedtools from compiled distribution into /opt/bedtools  
ENV BEDTOOLS_RELEASE=2.25.0  
ENV
BEDTOOLS_URL=https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_RELEASE}/bedtools-${BEDTOOLS_RELEASE}.tar.gz  
ENV DEST_DIR=/opt/  
# Download Bedtools, decompress, compile and remove unnecessary files  
RUN curl -SLo ${DEST_DIR}/bedtools-${BEDTOOLS_RELEASE}.tar.gz ${BEDTOOLS_URL}
&& \  
tar -xf ${DEST_DIR}/bedtools-${BEDTOOLS_RELEASE}.tar.gz -C ${DEST_DIR} && \  
rm ${DEST_DIR}/bedtools-${BEDTOOLS_RELEASE}.tar.gz && \  
cd ${DEST_DIR}/bedtools2 && \  
make && \  
mkdir ${DEST_DIR}/bedtools-${BEDTOOLS_RELEASE} && \  
mv bin/* ${DEST_DIR}/bedtools-${BEDTOOLS_RELEASE}/ && \  
rm -rf ${DEST_DIR}/bedtools2  
  
# Add bedtools path to the enviroment  
ENV PATH=${DEST_DIR}/bedtools-${BEDTOOLS_RELEASE}:$PATH  
  
CMD ["bedtools"]  

