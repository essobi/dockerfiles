FROM gcc:5.3  
MAINTAINER bmajoros@duke.edu  
  
# Installs ACE from sources into /opt/  
ENV DEST_DIR=/opt/  
  
# Install GSL  
ENV GSL_VERSION=2.2.1  
ENV GSL=http://mirror.thecodefactory.org/gnu/gsl/gsl-${GSL_VERSION}.tar.gz  
RUN curl -SLo ${DEST_DIR}/gsl-${GSL_VERSION}.tar.gz ${GSL} && \  
tar -xf ${DEST_DIR}/gsl-${GSL_VERSION}.tar.gz -C ${DEST_DIR} && \  
rm ${DEST_DIR}/gsl-${GSL_VERSION}.tar.gz && \  
cd ${DEST_DIR}/gsl-${GSL_VERSION} && \  
./configure && \  
make && \  
make install && \  
rm -rf ${DEST_DIR}/gsl-${GSL_VERSION}  
  
# Download and install kentUtikls  
RUN git clone git://github.com/ENCODE-DCC/kentUtils.git && \  
cd kentUtils && \  
make && \  
cp -r ./bin/* /opt/ && \  
cd .. && \  
rm -rf kentUtils  
  
# Download tabix from Samtools  
ENV TABIX_VERSION=0.2.6  
ENV
TABIX_URL=https://sourceforge.net/projects/samtools/files/tabix/tabix-${TABIX_VERSION}.tar.bz2/download  
RUN curl -SLo ${DEST_DIR}/tabix-${TABIX_VERSION}.tar.bz2 ${TABIX_URL} && \  
tar -xf ${DEST_DIR}/tabix-${TABIX_VERSION}.tar.bz2 -C ${DEST_DIR} && \  
rm ${DEST_DIR}/tabix-${TABIX_VERSION}.tar.bz2 && \  
cd ${DEST_DIR}/tabix-${TABIX_VERSION} && \  
make && \  
cp -r tabix ${DEST_DIR} && \  
rm -rf ${DEST_DIR}/tabix-${TABIX_VERSION}  
  
# Download and compile ACE libraries  
RUN cd ${DEST_DIR} && \  
mkdir ace && \  
cd ace && \  
git clone \--recursive git://github.com/bmajoros/ACE.git && \  
cd ACE && \  
make all  
  
# Download bgzip from htslib  
RUN git clone https://github.com/samtools/htslib.git && \  
cd htslib && \  
make && \  
make install  
  
# Setup the environment  
ENV PATH=${DEST_DIR}:${PATH}  
ENV TMPDIR=/tmp/  
ENV ACE=${DEST_DIR}/ace/ACE  
ENV PERLLIB=${DEST_DIR}/ace/ACE/perl  
ENV PATH=${DEST_DIR}/ace/ACE:${DEST_DIR}/ace/ACE/perl:${PATH}  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
# Default command for the image (when is run without any command)  
CMD ["ace.pl"]  

