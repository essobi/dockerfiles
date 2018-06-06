# Chinese segmentation tools for plaintext UTF-8 corpus.  
#  
# URL: https://github.com/William-Yeh/cseg  
#  
# Reference: https://github.com/ansjsun/ansj_seg  
#  
# Version 0.1  
#  
# pull base image  
FROM williamyeh/java8  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
ENV GRADLE_TARBALL
https://services.gradle.org/distributions/gradle-2.0-bin.zip  
ENV GRADLE_BIN /tmp/gradle-2.0/bin/gradle  
  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y curl git unzip && \  
\  
cd /tmp && \  
curl -OL $GRADLE_TARBALL && \  
unzip *.zip && \  
\  
\  
\  
cd /tmp && \  
git clone https://github.com/William-Yeh/cseg.git && \  
cd cseg && \  
$GRADLE_BIN download && \  
$GRADLE_BIN build && \  
\  
\  
\  
mkdir -p /opt/cseg /data/dict && \  
cd /tmp/cseg/build && \  
cp libs/cseg-all.jar /opt/cseg && \  
cp downloaded-resources/library.properties /opt/cseg && \  
cp downloaded-resources/library/* /data/dict && \  
sed -i -e 's/=library/=\/data\/dict/' /opt/cseg/library.properties  
\  
\  
\  
apt-get remove -y --auto-remove curl git unzip && \  
apt-get clean && \  
rm -rf /tmp/* /root/.gradle  
  
  
#----------------------------#  
# configure  
VOLUME [ "/data/file", "/data/dict" ]  
WORKDIR /data/file  
  
# for convenience  
ENV CSEG_PATH /opt/cseg  
ENV PATH $CSEG_PATH:$PATH  
ENV CLASSPATH $CSEG_PATH:$CSEG_PATH/cseg-all.jar  
COPY usage.sh /opt/cseg/  
COPY cseg /opt/cseg/  
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME  
  
# Define default command.  
CMD ["usage.sh"]  

