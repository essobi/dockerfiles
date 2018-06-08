FROM centos:centos6  
MAINTAINER Pierre CARRE <pierre.carre78@gmail.com>  
  
RUN cd /opt \  
&& curl -L 'https://s3.amazonaws.com/pierrecarre-java/oracle-
jdk/jdk-6u45-linux-x64.bin' \  
-o jdk-6u45-linux-x64.bin \  
&& chmod +x jdk-6u45-linux-x64.bin \  
&& yes yes | ./jdk-6u45-linux-x64.bin \  
&& rm -rf jdk-6u45-linux-x64.bin  
  
# Set environment variables.  
ENV HOME /root  
  
# Set JAVA_HOME  
ENV JAVA_HOME /opt/jdk1.6.0_45  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  

