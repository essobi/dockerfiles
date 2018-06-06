FROM comics/centos  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: samtools  
# Software Version: 1.1  
# Software Website: https://github.com/samtools/samtools/  
# Description: samtools  
##############################################################  
  
ENV APP_NAME=samtools  
ENV VERSION=1.1  
ENV GIT=https://github.com/BenLangmead/samtools.git  
ENV APPS=/software/applications  
ENV DEST=$APPS/$APP_NAME/  
ENV PATH=$APPS/$APP_NAME/$VERSION/bin:$APPS/bcftools/$VERSION/bin:$PATH  
  
RUN yum install -y zlib-devel \  
ncurses-devel ; \  
yum clean all ; \  
curl -L -o htslib-$VERSION.tar.gz
https://github.com/samtools/htslib/archive/$VERSION.tar.gz ; \  
curl -L -o samtools-$VERSION.tar.gz
https://github.com/samtools/samtools/archive/$VERSION.tar.gz ; \  
curl -L -o bcftools-$VERSION.tar.gz
https://github.com/samtools/bcftools/archive/$VERSION.tar.gz ; \  
tar xzf bcftools-$VERSION.tar.gz ; \  
tar xzf htslib-$VERSION.tar.gz ; \  
tar xzf samtools-$VERSION.tar.gz ; \  
rm -rf bcftools-$VERSION.tar.gz ; \  
rm -rf htslib-$VERSION.tar.gz ; \  
rm -rf samtools-$VERSION.tar.gz ; \  
mv htslib-$VERSION htslib ; \  
cd bcftools-$VERSION ; \  
make -j HTSDIR=../htslib ; \  
make prefix=$APPS/bcftools/$VERSION install ; \  
cd .. ; \  
cd samtools-$VERSION ; \  
make -j HTSDIR=../htslib ; \  
make prefix=$APPS/$APP_NAME/$VERSION install ; \  
cd ../ ; \  
rm -rf htslib samtools-$VERSION bcftools-$VERSION  
  
CMD ["/bin/bash"]  
  

