FROM centos:7  
MAINTAINER sdi  
  
# Build time arguments  
ARG JAVA_VERSION=${jdk_version:-1.8.0}  
  
RUN yum update -y && \  
yum install -y wget && \  
yum install -y java-$JAVA_VERSION-openjdk java-$JAVA_VERSION-openjdk-devel &&
\  
yum clean all  
  
# Set environment variables  
ENV HOME /root  
  
# Define working directory  
WORKDIR /root  
  
# Define default command  
CMD ["bash"]  

