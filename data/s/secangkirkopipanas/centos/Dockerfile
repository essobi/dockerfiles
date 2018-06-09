FROM centos:latest  
MAINTAINER Robertus Lilik Haryanto <robert.djokdja@gmail.com>  
  
# Upgrade and install additional softwares  
RUN \  
echo "### Upgrade and install additional softwares" && \  
yum -y upgrade && \  
yum -y install nano wget zip telnet && \  
yum clean all  
  
# Downloading Java  
RUN \  
yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel && \  
yum clean all  
  
# Configure environment variables  
ENV TZ Asia/Singapore  
  
# Define default command  
CMD ["/bin/bash"]

