# Dockerizing a base images with:  
#  
# - Ubuntu 14.04  
# - Oracle JDK 7u71  
#  
# Build: docker build -t exoplatform/ubuntu-jdk7:7u71 .  
#  
# Run: docker run -t -i exoplatform/ubuntu-jdk7:7u71 bash  
FROM ubuntu:14.04  
MAINTAINER DROUET Frederic <fdrouet+docker@exoplatform.com>  
  
# Install some useful or needed tools  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -qq update && \  
apt-get -qq -y upgrade && \  
apt-get -qq -y install wget curl unzip htop && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y autoclean  
  
# Create needed directories  
ENV DOWNLOAD_DIR /srv/downloads  
RUN mkdir -p "${DOWNLOAD_DIR}"  
  
# Add some aliases  
RUN echo "alias ll='ls -al --color'" > /etc/profile.d/aliases.sh  
  
# Install Oracle Java 7 SDK  
ENV JVM_DIR /usr/lib/jvm  
RUN mkdir -p "${JVM_DIR}"  
  
#WORKDIR ${JVM_DIR}  
RUN wget -q --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" -O "${DOWNLOAD_DIR}/jdk-7u71-linux-x64.tar.gz"
"http://download.oracle.com/otn-
pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.tar.gz" && \  
cd "${JVM_DIR}" && \  
tar -xzf "${DOWNLOAD_DIR}/jdk-7u71-linux-x64.tar.gz" && \  
rm -f "${DOWNLOAD_DIR}/jdk-7u71-linux-x64.tar.gz" && \  
mv "${JVM_DIR}/jdk1.7.0_71" "${JVM_DIR}/java-1.7.0_71-oracle-x64" && \  
ln -s "${JVM_DIR}/java-1.7.0_71-oracle-x64" "${JVM_DIR}/java-1.7.0-oracle-x64"  
ADD java-1.7.0-oracle-x64.jinfo ${JVM_DIR}/.java-1.7.0-oracle-x64.jinfo  
RUN cat "${JVM_DIR}/.java-1.7.0-oracle-x64.jinfo" | grep -E '^(jre|jdk|hl)' |
awk '{print "/usr/bin/" $2 " " $2 " " $3 " 30 \n"}' | xargs -t -n4 sudo
update-alternatives --install  
ENV JAVA_HOME ${JVM_DIR}/java-1.7.0-oracle-x64  

