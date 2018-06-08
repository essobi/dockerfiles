FROM centos:centos6  
MAINTAINER Nicolas Grange "grange74@gmail.com"  
# Download Java 6 from the Oracle site and Install  
# We are chaining all these commands to reduce the size of the image  
# it does unfortunately make it less readable so i try to explain each step:  
# 1. download/install wget  
# 2. pull down the Oracle Java 6 rpm bin file using wget  
# 3. change permissions on the download bin file to make it executable  
# 4. extract the bin file into an rpm  
# 5. delete the bin file  
# 6. install Java 6 via the rpm  
# 7. delete the rpm file  
# 8. ask yum to clean itself up  
RUN yum -y install wget && \  
wget --no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/6u45-b06/jre-6u45-linux-x64-rpm.bin" \  
-O /tmp/jre-6u45-linux-x64-rpm.bin && \  
chmod a+x /tmp/jre-6u45-linux-x64-rpm.bin && \  
/tmp/jre-6u45-linux-x64-rpm.bin -x && \  
rm /tmp/jre-6u45-linux-x64-rpm.bin && \  
yum -y localinstall /jre-6u45-linux-amd64.rpm && \  
rm /jre-6u45-linux-amd64.rpm && \  
yum clean all  
  
ENV JAVA_HOME /usr/java/default

