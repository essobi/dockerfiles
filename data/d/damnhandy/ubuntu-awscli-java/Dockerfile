FROM ubuntu-debootstrap:14.04.3  
MAINTAINER Ryan J. McDonough "ryan@damnhandy.com"  
# Install python, pip, awscli and the Oracle Java Server JRE  
RUN dpkg-reconfigure -f noninteractive locales && locale-gen en_US.UTF-8 && \  
echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list && \  
apt-get -y update && \  
apt-get install -y curl python-pip && \  
pip --no-input install awscli && \  
apt-get clean && \  
curl -L -b "oraclelicense=a" http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz | tar xzv -C /usr/local && \  
ln -s /usr/local/jdk1.8.0_66 /usr/local/java  
# Set the locale to UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_COLLATE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV JAVA_HOME /usr/local/java  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
CMD ["bash"]  

