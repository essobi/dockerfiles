FROM sglim2/centos7  
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
  
RUN yum install -y bzip2 ; \  
git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
make -j ; \  
make trinity_essentials ; \  
make plugins ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
cd ../ ; \  
mv $APP_NAME $DEST/$VERSION  
CMD ["/bin/bash"]  
  

