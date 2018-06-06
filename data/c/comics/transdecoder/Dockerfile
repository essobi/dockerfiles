FROM comics/centos  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: TransDecoder  
# Software Version: 3.0.1  
# Software Website: https://github.com/TransDecoder/TransDecoder  
# Description: Identification of candidate coding regions within transcript
sequences  
##############################################################  
  
ENV APP_NAME=TransDecoder  
ENV VERSION=v3.0.1  
ENV GIT=https://github.com/TransDecoder/TransDecoder  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION/:$DEST/$VERSION/util:$DEST/$VERSION/util/bin:$PATH  
  
RUN yum install -y perl-App-cpanminus ; \  
yum clean all ; \  
cpanm Data::Dumper ; \  
cpanm DB_File ; \  
git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
rm -rf .git ; \  
make ; \  
mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \  
cp LICENSE.txt /usr/share/licenses/$APP_NAME-$VERSION/ ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
mv $APP_NAME $DEST/$VERSION  
CMD ["/bin/bash"]  
  

