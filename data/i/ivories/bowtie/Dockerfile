FROM sequenceiq/spark:1.6.0  
ENV APP_NAME=bowtie2  
ENV VERSION=v2.2.9  
ENV GIT=https://github.com/BenLangmead/bowtie2/archive/v2.2.9.tar.gz  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION/:$DEST/$VERSION/scripts/:$PATH  
  
RUN curl -o v2.2.9.tar.gz
https://codeload.github.com/BenLangmead/bowtie2/tar.gz/v2.2.9 ; \  
tar zxvf v2.2.9.tar.gz ; \  
cd bowtie2-2.2.9 ; \  
sed -i "s#^prefix.*#prefix = $DEST#" Makefile ; \  
make -j ; \  
mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \  
cp LICENSE /usr/share/licenses/$APP_NAME-$VERSION/ ; \  
cd ../ ; \  
mkdir -p $DEST ;  
  
RUN touch /var/lib/rpm/* ; \  
yum install -y wget ; \  
touch /var/lib/rpm/* ; \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.rpm ; \  
yum localinstall -y jdk-8u111-linux-x64.rpm ; \  
rm -rf jdk-8u111-linux-x64.rpm  
  
RUN mv bowtie2-2.2.9 $DEST/$VERSION  
  
# Installs bowtie from compiled distribution into /opt/bowtie  
ENV DEST_DIR=/opt  
  
# Download Bowtie, unzip it and remove .zip file  
RUN curl -SLo ${DEST_DIR}/bowtie.zip
http://pilotfiber.dl.sourceforge.net/project/bowtie-
bio/bowtie/1.1.2/bowtie-1.1.2-linux-x86_64.zip && unzip ${DEST_DIR}/bowtie.zip
-d ${DEST_DIR} && rm ${DEST_DIR}/bowtie.zip  
  
RUN touch /var/lib/rpm/* && yum -y install boost-devel  
RUN curl -SLo tophat-2.1.1.tar.gz
https://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.tar.gz  
RUN tar zxvf tophat-2.1.1.tar.gz && cd tophat-2.1.1 && ./configure && make &&
make install  
  
# Add bowtie path to the enviroment  
ENV PATH=${DEST_DIR}/bowtie2-${BOWTIE_RELEASE}:$PATH  
ENV PATH=/opt/bowtie-1.1.2:$PATH  
  
  
CMD ["/bin/bash"]  

