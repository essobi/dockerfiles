FROM comics/centos  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: busco  
# Software Version: 3.0.2  
# Software Website: http://busco.ezlab.org/  
# Description: Assessing genome assembly and annotation completeness with
Benchmarking Universal Single-Copy Orthologs  
##############################################################  
  
ENV APP_NAME=busco  
ENV VERSION=3.0.2  
ENV BLASTVERSION=2.4.0  
ENV HMMERVERSION=3.1b2  
ENV AUGUSTUSVERSION=3.2.2  
ENV GIT=https://gitlab.com/ezlab/busco.git  
ENV APPS=/software/applications  
ENV DEST=${APPS}/${APP_NAME}/  
ENV PATH=${APPS}/${APP_NAME}/${VERSION}/scripts:$PATH  
ENV PATH=${APPS}/hmmer/${HMMERVERSION}/bin:$PATH  
ENV PATH=${APPS}/augustus/${AUGUSTUSVERSION}/bin:$PATH  
ENV PATH=${APPS}/augustus/${AUGUSTUSVERSION}/scripts:$PATH  
ENV AUGUSTUS_CONFIG_PATH=${APPS}/augustus/${AUGUSTUSVERSION}/config/  
  
# BLAST  
RUN yum install -y \  
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLASTVERSION}/ncbi-
blast-${BLASTVERSION}+-2.x86_64.rpm \  
parallel  
  
# HMMER...  
RUN cd /tmp ; \  
curl -L -o hmmer-${HMMERVERSION}.tar.gz
http://eddylab.org/software/hmmer3/${HMMERVERSION}/hmmer-${HMMERVERSION}.tar.gz
; \  
tar xzf hmmer-${HMMERVERSION}.tar.gz ; \  
cd hmmer-${HMMERVERSION} ; \  
./configure --prefix=${APPS}/hmmer/${HMMERVERSION} ; \  
make -j ; \  
make install ; \  
mkdir -p /usr/share/licenses/hmmer-${HMMERVERSION} ; \  
cp LICENSE /usr/share/licenses/hmmer-${HMMERVERSION}/ ; \  
cd ../ ; \  
rm -rf hmmer-${HMMERVESION}.tar.gz hmmer-${HMMERVERSION}  
  
# Augustus...  
RUN yum install -y \  
boost \  
boost-devel \  
gsl \  
gsl-devel \  
lpsolve \  
lpsolve-devel \  
sqlite \  
sqlite-devel \  
suitesparse \  
suitesparse-devel \  
wget \  
zlib-devel ; \  
cd /tmp ; \  
wget http://bioinf.uni-
greifswald.de/augustus/binaries/old/augustus-${AUGUSTUSVERSION}.tar.gz ; \  
tar xzf augustus-${AUGUSTUSVERSION}.tar.gz ; \  
cd augustus-${AUGUSTUSVERSION} ; \  
sed -i 's/^#.*\\(SQLITE.*=.*true\\)/\1/' common.mk ; \  
sed -i 's/^#.*\\(COMPGENEPRED.*=.*true\\)/\1/' common.mk ; \  
make ; \  
sed -i "s|\\(^INSTALLDIR.*=\\).*|\1 ${APPS}/augustus/${AUGUSTUSVERSION}|"
Makefile ; \  
make install ; \  
cd .. ; \  
rm -rf augustus-${AUGUSTUSVERSION}.tar.gz augustus-${AUGUSTUSVERSION}  
  
# busco...  
RUN yum install -y \  
python34 \  
python34-devel \  
R-core ; \  
yum update -y; \  
yum clean all ; \  
mkdir -p ${APPS}/${APP_NAME} ; \  
cd ${APPS}/${APP_NAME} ; \  
git clone ${GIT} ${VERSION}; \  
cd ${VERSION} ; \  
git checkout tags/${VERSION} ; \  
python setup.py install ; \  
python3 setup.py install ; \  
cp config/config.ini.default config/config.ini ; \  
sed -i "s|\\(^;cpu = \\).*|;cpu = 8|" config/config.ini ; \  
sed -i "s|\\(^;blast_single_core = \\).*|;blast_single_core = False|"
config/config.ini ; \  
sed -i '/^# path to augustus$/!b;n;cpath =
/software/applications/augustus/3.2.2/bin/' config/config.ini ; \  
sed -i '/^# path to augustus etraining$/!b;n;cpath =
/software/applications/augustus/3.2.2/bin/' config/config.ini ; \  
sed -i '/^\\[gff2gbSmallDNA.pl\\]/!b;n;cpath =
/software/applications/augustus/3.2.2/scripts/' config/config.ini ; \  
sed -i '/^\\[new_species.pl\\]/!b;n;cpath =
/software/applications/augustus/3.2.2/scripts/' config/config.ini ; \  
sed -i '/^\\[optimize_augustus.pl\\]/!b;n;cpath =
/software/applications/augustus/3.2.2/scripts/' config/config.ini ; \  
sed -i '/^# path to HMMsearch executable$/!b;n;cpath =
/software/applications/hmmer/3.1b2/bin/' config/config.ini  
  
CMD ["/bin/bash"]  
  

