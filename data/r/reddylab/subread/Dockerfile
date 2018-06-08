FROM phusion/baseimage  
MAINTAINER Alejandro Barrera <alejandro.barrera@duke.edu>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
curl  
  
# Define ENV variables for download  
ENV SUBREAD_RELEASE=1.4.6-p4  
ENV
SUBREAD_URL=https://sourceforge.net/projects/subread/files/subread-${SUBREAD_RELEASE}/subread-${SUBREAD_RELEASE}-Linux-x86_64.tar.gz/download  
ENV DEST_DIR=/opt  
  
# Download and unzip subread compiled package, removing unnecessary files
afterwards  
RUN curl -SLo ${DEST_DIR}/SUBREAD-${SUBREAD_RELEASE}.tar.gz ${SUBREAD_URL} &&
\  
tar xzvf ${DEST_DIR}/SUBREAD-${SUBREAD_RELEASE}.tar.gz -C ${DEST_DIR} && \  
rm ${DEST_DIR}/SUBREAD-${SUBREAD_RELEASE}.tar.gz  
  
# Add subread binaries to path  
ENV
PATH=${DEST_DIR}/subread-${SUBREAD_RELEASE}-Linux-x86_64/bin/:${DEST_DIR}/subread-${SUBREAD_RELEASE}-Linux-x86_64/bin/utilities/:$PATH  
# List executables from subread  
CMD ["find", "/opt/", "-executable", "-type", "f"]  

