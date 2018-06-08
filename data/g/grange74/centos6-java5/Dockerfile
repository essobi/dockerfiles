FROM centos:centos6  
MAINTAINER Nicolas Grange "grange74@gmail.com"  
# Download Java 5 from the Oracle site and Install  
# We are chaining all these commands to reduce the size of the image  
# it does unfortunately make it less readable so i try to explain each step:  
# 1. download/install wget  
# 2. pull down the Oracle Java 5 rpm bin file using wget  
# 3. change directory to where Java 5 was downloaded to  
# 3. change permissions on the download bin file to make it executable  
# 4. install Java 5 via the rpm  
# 5. delete the rpm & bin files  
# 6. ask yum to clean itself up  
RUN yum -y install wget && \  
wget --no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-pub/java/jdk/1.5.0_22/jre-1_5_0_22-linux-
amd64-rpm.bin" \  
-O /tmp/jre-1_5_0_22-linux-amd64-rpm.bin && \  
cd /tmp && \  
chmod a+x jre-1_5_0_22-linux-amd64-rpm.bin && \  
sh -c './jre-1_5_0_22-linux-amd64-rpm.bin >/dev/null <<< "" <<< y >/dev/null
<<< "" <<< y' && \  
rm jre-1_5_0_22-linux-* && \  
yum clean all  
  
ENV JAVA_HOME /usr/java/jre1.5.0_22  
ENV PATH $JAVA_HOME/bin:$PATH:$HOME/bin

