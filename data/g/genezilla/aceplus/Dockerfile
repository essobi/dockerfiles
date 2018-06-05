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
  
# Install R  
RUN wget https://cloud.r-project.org/src/base/R-3/R-3.4.3.tar.gz && \  
tar xvfz R-3.4.3.tar.gz && \  
cd R-3.4.3 && \  
./configure && \  
make  
  
# Install R package "glmnet"  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN /R-3.4.3/bin/Rscript -e "install.packages('glmnet')"  
  
# Install python version 3.6  
RUN wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz && \  
tar xvfz Python-3.6.3.tgz && \  
cd Python-3.6.3 && \  
./configure && \  
make  
  
# Put env in /bin so our scripts can call it normally  
RUN cp /usr/bin/env /bin  
  
# Download and install kentUtils  
RUN git clone git://github.com/ENCODE-DCC/kentUtils.git && \  
cd kentUtils && \  
make && \  
cp -r ./bin/* /opt/ && \  
cd .. && \  
rm -rf kentUtils  
  
# Download tabix from Samtools  
#ENV TABIX_VERSION=0.2.6  
#ENV
TABIX_URL=https://sourceforge.net/projects/samtools/files/tabix/tabix-${TABIX_VERSION}.tar.bz2/download  
#RUN curl -SLo ${DEST_DIR}/tabix-${TABIX_VERSION}.tar.bz2 ${TABIX_URL} && \  
# tar -xf ${DEST_DIR}/tabix-${TABIX_VERSION}.tar.bz2 -C ${DEST_DIR} && \  
# rm ${DEST_DIR}/tabix-${TABIX_VERSION}.tar.bz2 && \  
# cd ${DEST_DIR}/tabix-${TABIX_VERSION} && \  
# make && \  
# cp -r tabix ${DEST_DIR} && \  
# rm -rf ${DEST_DIR}/tabix-${TABIX_VERSION}  
# Download bgzip from htslib  
RUN git clone https://github.com/samtools/htslib.git && \  
cd htslib && \  
make && \  
make install  
  
RUN git clone \--recursive https://github.com/bmajoros/ACE.git && \  
export TMPDIR=/tmp && \  
export ACE=/ACE && \  
export ACEPLUS=/ACE && \  
export PERLLIB=/ACE/perl && \  
export PYTHONPATH=/ACE/python && \  
cd ACE && \  
make all  
  
RUN cp /ACE/pam10 /root  
  
# Setup the environment  
ENV ACE=/ACE  
ENV ACEPLUS=/ACE  
ENV PERLLIB=/ACE/perl  
ENV PYTHONPATH=/ACE/python  
ENV
PATH=${DEST_DIR}:/R-3.4.3/bin:/Python-3.6.3:${ACEPLUS}:${ACEPLUS}/perl:${ACEPLUS}/python:${PATH}  
ENV TMPDIR=/tmp/  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
  

