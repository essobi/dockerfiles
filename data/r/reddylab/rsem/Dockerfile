FROM phusion/baseimage  
MAINTAINER Alejandro Barrera <alejandro.barrera@duke.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
g++ \  
zlib1g-dev \  
libncurses-dev \  
curl \  
unzip  
  
#########################################################  
# NOTE: Added here Bowtie image given that CWL #  
# ^^^^ will not allow multiple Docker dependencies #  
# at this point. #  
#########################################################  
# Installs bowtie from compiled distribution into /opt/bowtie  
ENV BOWTIE_URL=http://sourceforge.net/projects/bowtie-bio/files/bowtie  
ENV BOWTIE_RELEASE=0.12.9  
ENV DEST_DIR=/opt  
  
# Download Bowtie, unzip it and remove .zip file  
RUN curl -SLo ${DEST_DIR}/bowtie-${BOWTIE_RELEASE}.zip
${BOWTIE_URL}/${BOWTIE_RELEASE}/bowtie-${BOWTIE_RELEASE}-linux-x86_64.zip &&
unzip ${DEST_DIR}/bowtie-${BOWTIE_RELEASE}.zip -d ${DEST_DIR} && rm
${DEST_DIR}/bowtie-${BOWTIE_RELEASE}.zip  
  
# Add bowtie path to the enviroment  
ENV PATH=${DEST_DIR}/bowtie-${BOWTIE_RELEASE}:$PATH  
  
# Define ENV variables for download  
ENV RSEM_RELEASE=1.2.25  
ENV RSEM_URL=https://github.com/deweylab/RSEM/archive/v${RSEM_RELEASE}.tar.gz  
ENV DEST_DIR=/opt  
  
# Download and unpack RSEM sources, make & install and remove unnecessary
files  
RUN curl -SLo ${DEST_DIR}/RSEM-${RSEM_RELEASE}.tar.gz ${RSEM_URL} && \  
tar xzvf ${DEST_DIR}/RSEM-${RSEM_RELEASE}.tar.gz -C ${DEST_DIR} && \  
cd ${DEST_DIR}/RSEM-${RSEM_RELEASE} && \  
make && \  
rm -rf ${DEST_DIR}/RSEM-${RSEM_RELEASE}.tar.gz  
  
# Add RSEM path to ENV path  
ENV PATH=${DEST_DIR}/RSEM-${RSEM_RELEASE}/:$PATH  
  
# List executables provided by rsem  
CMD ["find", "/opt/", "-executable", "-type", "f", "-iname", "rsem*"]  
  

