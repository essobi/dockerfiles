FROM r-base:3.2.4  
RUN apt-get update && apt-get install -y \  
libboost-all-dev \  
curl \  
build-essential \  
libncurses-dev \  
zlib1g-dev \  
gawk  
  
# Installs samtools from sources into /opt/  
ENV SAMTOOLS_RELEASE=1.3  
ENV SAMTOOLS_URL=https://github.com/samtools/samtools/releases/download/  
ENV DEST_DIR=/opt/  
  
# Download Samtools; untar & decompress; remove tr.bz2 file; compile & install
samtools; remove unnecessary files  
RUN curl -SLo ${DEST_DIR}/samtools-${SAMTOOLS_RELEASE}.tar.bz2
${SAMTOOLS_URL}/${SAMTOOLS_RELEASE}/samtools-${SAMTOOLS_RELEASE}.tar.bz2 && \  
tar -xf ${DEST_DIR}/samtools-${SAMTOOLS_RELEASE}.tar.bz2 -C ${DEST_DIR} && \  
rm ${DEST_DIR}/samtools-${SAMTOOLS_RELEASE}.tar.bz2 && \  
cd ${DEST_DIR}/samtools-${SAMTOOLS_RELEASE} && \  
./configure && \  
make && \  
make install && \  
rm -rf ${DEST_DIR}/samtools-${SAMTOOLS_RELEASE}  
  
ENV SPP_VERSION=1.13  
WORKDIR /usr/local/src/rscripts  
  
# Download and install SPP and auxiliary R packages; remove unnecessary files  
RUN printf
'source("https://bioconductor.org/biocLite.R")\nbiocLite("Rsamtools")\n' >
install_Rsamtools.R && \  
Rscript install_Rsamtools.R && \  
curl -SLo ./spp_${SPP_VERSION}.tar.gz https://github.com/hms-
dbmi/spp/archive/${SPP_VERSION}.tar.gz && \  
curl -SLo ./bitops_1.0-6.tar.gz
https://cran.r-project.org/src/contrib/bitops_1.0-6.tar.gz && \  
curl -SLo ./caTools_1.17.1.tar.gz
https://cran.r-project.org/src/contrib/caTools_1.17.1.tar.gz && \  
R CMD INSTALL bitops_1.0-6.tar.gz && \  
R CMD INSTALL caTools_1.17.1.tar.gz && \  
R CMD INSTALL spp_${SPP_VERSION}.tar.gz && \  
rm -f ./spp_${SPP_VERSION}.tar.gz ./bitops_1.0-6.tar.gz
./caTools_1.17.1.tar.gz ./install_Rsamtools.R  
  
# Download and install run_spp.R package; remove unnecessary files  
RUN curl -SLo ./run_spp.R.origin
https://raw.githubusercontent.com/crazyhottommy/phantompeakqualtools/master/run_spp.R
&& \  
printf '#!/usr/bin/env Rscript\n' > ./run_spp.R && \  
cat ./run_spp.R.origin >> ./run_spp.R && \  
chmod +x run_spp.R && \  
rm -f ./run_spp.R.origin  
  
# Add rscripts folder to PATH  
ENV PATH=/usr/local/src/rscripts:$PATH  
CMD ["run_spp.R"]  

