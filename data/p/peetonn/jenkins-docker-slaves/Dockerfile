FROM ubuntu:12.04  
MAINTAINER peter@remap.ucla.edu  
  
ADD ./slave.jar /  
ADD ./run-slave.sh /  
RUN chmod +x /run-slave.sh && \  
apt-get update && apt-get install -y \  
build-essential pkg-config \  
git cmake wget curl ntp \  
python-software-properties \  
software-properties-common \  
libgtk2.0-dev  
  
# Java  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment && \  
echo "source /etc/environment" >> ~/.bashrc  
  
# NDN-CPP  
RUN apt-get install -y libssl-dev  
  
# NDN-RTC  
# default ubuntu 12.04 repo does't have boost1.54 (required for NDN-RTC)  
RUN add-apt-repository -y ppa:libreoffice/ppa && apt-get update -y && \  
apt-get install -y libboost1.54-all-dev  
  
# install g++4.8 for C++11 support  
# http://ubuntuhandbook.org/index.php/2013/08/install-gcc-4-8-via-ppa-in-
ubuntu-12-04-13-04/  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test && apt-get update &&\  
apt-get install -y gcc-4.8 g++-4.8 && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20 && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20 && \  
update-alternatives --config gcc && \  
update-alternatives --config g++  
  
CMD /run-slave.sh

