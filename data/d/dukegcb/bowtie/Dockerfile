FROM phusion/baseimage  
MAINTAINER Alejandro Barrera <alejandro.barrera@duke.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
curl \  
unzip  
  
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
  
CMD ["bowtie"]  

