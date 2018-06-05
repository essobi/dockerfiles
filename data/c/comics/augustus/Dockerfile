FROM comics/bamtools  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Software: augustus  
# Software Version: 3.2.2  
# Software Website: http://bioinf.uni-greifswald.de/augustus  
# Description: predicts genes in eukaryotic genomic sequences  
##############################################################  
  
ENV APP_NAME=augustus  
ENV VERSION=3.2.2  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION/bin:$PATH  
  
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
yum update -y; \  
yum clean all ; \  
wget http://bioinf.uni-
greifswald.de/augustus/binaries/old/augustus-$VERSION.tar.gz ; \  
tar xzf augustus-$VERSION.tar.gz ; \  
cd augustus-$VERSION ; \  
sed -i 's/^#.*\\(SQLITE.*=.*true\\)/\1/' common.mk ; \  
sed -i 's/^#.*\\(COMPGENEPRED.*=.*true\\)/\1/' common.mk ; \  
make ; \  
sed -i "s|\\(^INSTALLDIR.*=\\).*|\1 $DEST/$VERSION|" Makefile ; \  
make install ; \  
cd .. ; \  
rm -rf augustus-$VERSION.tar.gz augustus-$VERSION  
CMD ["/bin/bash"]  
  

