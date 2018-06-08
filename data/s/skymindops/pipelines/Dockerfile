FROM nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04  
  
RUN apt-get update && \  
apt-get -y \--no-install-recommends install \  
wget \  
curl \  
maven \  
ca-certificates \  
software-properties-common \  
git \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JAVA_PACKAGE_VERSION 8u131  
ENV JAVA_PACKAGE_NAME jdk-${JAVA_PACKAGE_VERSION}-linux-x64.tar.gz  
ENV JAVA_DOWNLOAD_URL http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/${JAVA_PACKAGE_NAME}  
ENV JAVA_HOME /opt/java  
  
RUN mkdir -p /opt && \  
# Switch from fecth jdk with curl to wget, because of errors during the fetch  
wget \--no-cookies \--no-check-certificate \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
${JAVA_DOWNLOAD_URL} && \  
tar -xzf ${JAVA_PACKAGE_NAME} -C /opt && \  
rm ${JAVA_PACKAGE_NAME} && \  
mv /opt/jdk* ${JAVA_HOME} && \  
update-alternatives \--install /usr/bin/java java ${JAVA_HOME}/bin/java 100 &&
\  
update-alternatives \--set java ${JAVA_HOME}/bin/java && \  
update-alternatives \--install /usr/bin/javac javac ${JAVA_HOME}/bin/javac 100
&& \  
update-alternatives \--set javac ${JAVA_HOME}/bin/javac  
  
RUN mkdir -p /opt/sbt && \  
curl -fsSL https://dl.bintray.com/sbt/native-
packages/sbt/0.13.13/sbt-0.13.13.tgz \  
| tar -xzC /opt/sbt \--strip-components=1  
  
RUN mkdir -p /opt/cmake && \  
curl -fsSL https://cmake.org/files/v3.9/cmake-3.9.0-Linux-x86_64.tar.gz \  
| tar -xzC /opt/cmake \--strip-components=1  
  
ENV PROTOBUF_PACKAGE_VERSION 3.5.0  
ENV PROTOBUF_PACKAGE_NAME protobuf-cpp-${PROTOBUF_PACKAGE_VERSION}.tar.gz  
ENV PROTOBUF_DOWNLOAD_URL
https://github.com/google/protobuf/releases/download/v${PROTOBUF_PACKAGE_VERSION}/${PROTOBUF_PACKAGE_NAME}  
ENV PROTOBUF_HOME /opt/protobuf  
  
RUN curl -fsSL ${PROTOBUF_DOWNLOAD_URL} \  
| tar xz && \  
cd protobuf-${PROTOBUF_PACKAGE_VERSION} && \  
./configure \--prefix=${PROTOBUF_HOME} && \  
make -j2 && \  
make install && \  
cd .. && \  
rm -r protobuf-${PROTOBUF_PACKAGE_VERSION}  
  
# Install git lfs for dl4j-test-resources  
#RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
# DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
git-lfs && \  
# git lfs install && \  
# rm -r /var/lib/apt/lists/*  
  
RUN groupadd jenkins -g 1000 && useradd -u 1000 -g 1000 -m jenkins  
  
ENV PATH /opt/sbt/bin:/opt/cmake/bin:${PROTOBUF_HOME}/bin:${PATH}  
  
USER jenkins  
  
CMD ["cat"]  

