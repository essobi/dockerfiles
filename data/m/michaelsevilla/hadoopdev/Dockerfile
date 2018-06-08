FROM sequenceiq/hadoop-docker:2.7.1  
MAINTAINER Michael Sevilla  
  
# install deps  
RUN echo "===> Installing jxio stuff..." && \  
DEBIAN_FRONTEND=noninteractive yum update -y && \  
yum groupinstall "Infiniband Support" -y  
RUN yum install -y \  
git \  
gcc-c++ \  
java-1.7.0-openjdk-devel \  
libtool \  
autoconf \  
automake \  
infiniband-diags \  
perftest \  
libibverbs-utils \  
librdmacm-utils \  
librdmacm-devel \  
libibverbs-devel \  
numactl \  
numactl-devel \  
libaio-devel \  
libevent-devel  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.95.x86_64/  
  
# Not sure why this failing right now  
#RUN echo "===> Build jxio..." && \  
# cd / && \  
# git clone https://github.com/accelio/JXIO.git && \  
# cd /JXIO && \  
# git clean -fd && \  
# ./build.sh  
ENV MAVEN_VERSION 3.3.3  
RUN echo "===> Install maven..." && \  
curl -fsSL
https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share && \  
mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven && \  
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
VOLUME /root/.m2  
  
ADD entrypoint.sh /  
RUN chmod 750 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

