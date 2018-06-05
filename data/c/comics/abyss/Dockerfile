FROM comics/centos  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Software: abyss  
# Software Version: 2.0.2  
# Software Website: https://github.com/bcgsc/abyss  
# Description: de novo sequence assembler intended for short paired-end reads
and large genomes  
##############################################################  
  
ENV APP_NAME=abyss  
ENV VERSION=2.0.2  
ENV GIT=https://github.com/bcgsc/abyss.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION/bin:$PATH  
  
RUN yum install -y autoconf \  
automake \  
boost-devel \  
sparsehash-devel ; \  
yum clean all ; \  
git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
./autogen.sh ; \  
./configure --prefix=$DEST/$VERSION ; \  
make -j ; \  
make install ; \  
mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \  
cp COPYRIGHT /usr/share/licenses/$APP_NAME-$VERSION/ ; \  
cd ../ ; \  
rm -rf $APP_NAME  
CMD ["/bin/bash"]  
  

