FROM comics/samtools  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: trinityrnaseq  
# Software Version: 2.2.0  
# Software Website: https://github.com/trinityrnaseq/trinityrnaseq  
# Description: Trinity RNA-Seq de novo transcriptome assembly  
##############################################################  
  
ENV APP_NAME=trinityrnaseq  
ENV VERSION=v2.2.0  
ENV GIT=https://github.com/trinityrnaseq/trinityrnaseq.git  
ENV LD_LIBRARY_PATH=/software/applications/trinityrnaseq/v2.2.0/trinity-
plugins/htslib  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION:$PATH  
ENV PATH=$DEST/$VERSION/util:$PATH  
ENV PATH=$DEST/$VERSION/util/support_scripts:$PATH  
ENV PATH=$DEST/$VERSION/util/misc:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/splice_path_analysis:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/iso_reco_analysis:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/blat_util:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/bam_gene_tests:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/altsplice_simulation_toolkit:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/TEST_SUPPORT/BFLY_TESTING:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/Monarch_util:$PATH  
ENV PATH=$DEST/$VERSION/util/misc/Artemis:$PATH  
  
  
RUN yum install -y bzip2 \  
java \  
ncurses-devel \  
perl-Data-Dumper \  
zlib-devel ; \  
yum clean all ; \  
git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
rm -rf .git ; \  
sed -i 's/^\\(trinity_essentials:.*\\) samtools/\1 /g' Makefile ; \  
make -j ; \  
make trinity_essentials ; \  
make plugins ; \  
mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \  
cp LICENSE.txt /usr/share/licenses/$APP_NAME-$VERSION/ ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
cd ../ ; \  
mv $APP_NAME $DEST/$VERSION  
CMD ["/bin/bash"]  
  

