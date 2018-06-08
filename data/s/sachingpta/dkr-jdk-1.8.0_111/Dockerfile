# Set the base image to sachingpta/dkr-ubuntu-15.10-x64.  
FROM sachingpta/dkr-ubuntu-15.10-x64  
  
# Author or maintainer of this image file  
MAINTAINER Sachin Gupta <sachin.aut@gmail.com>  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  
  
# All packages must work in noninteractive mode.  
ENV DEBIAN_FRONTEND noninteractive  
RUN export DEBIAN_FRONTEND=noninteractive  
  
#-------------------------------------------------------------------  
# Install JDK v1.8.0_111  
#-------------------------------------------------------------------  
RUN mkdir /opt/jdk && \  
cd /opt && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz && \  
tar -zxf jdk-8u111-linux-x64.tar.gz -C /opt/jdk && \  
update-alternatives --install /usr/bin/java java
/opt/jdk/jdk1.8.0_111/bin/java 100 && \  
update-alternatives --install /usr/bin/javac javac
/opt/jdk/jdk1.8.0_111/bin/javac 100 && \  
rm -rf jdk-8u111-linux-x64.tar.gz && \  
cd /  
  
# Verify installed version  
RUN java -version  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

