FROM comics/centos:latest  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: trimmomatic  
# Software Version: 0.36  
# Software Website: http://www.usadellab.org  
# Description: A flexible read trimming tool for Illumina NGS data  
##############################################################  
  
ENV APP_NAME=Trimmomatic  
ENV VERSION=0.36  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION:$PATH  
ENV TRIMMOMATIC=$DEST/$VERSION/trimmomatic-$VERSION.jar  
ENV ADAPTERPATH=$DEST/$VERSION/adapters  
  
RUN yum install -y unzip java ; \  
yum clean all ; \  
curl -L -o $APP_NAME-$VERSION.zip \  
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-$VERSION.zip
; \  
unzip $APP_NAME-$VERSION.zip ; \  
rm -f $APP_NAME-$VERSION.zip ; \  
mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \  
cp $APP_NAME-$VERSION/LICENSE /usr/share/licenses/$APP_NAME-$VERSION/ ; \  
mkdir -p $DEST ; \  
mv $APP_NAME-$VERSION $DEST/$VERSION  
  
CMD ["/bin/bash"]  
  

