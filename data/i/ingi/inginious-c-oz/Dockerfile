# DOCKER-VERSION 1.1.0  
#inherit from the base container, which have all the needed script to launch
tasks  
FROM ingi/inginious-c-base  
LABEL org.inginious.grading.name="oz"  
  
RUN yum -y install \  
java-1.7.0-openjdk \  
java-1.7.0-openjdk-devel \  
ant ant-junit \  
bc enca \  
emacs tcl tk boost \  
ImageMagick \  
Xvfb \  
wget \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum  
  
ADD mozart2-2.0.0-alpha.0+build.4105.5c06ced-x86_64-linux.rpm /mozart.rpm  
  
RUN rpm -ivh /mozart.rpm && \  
rm /mozart.rpm  
  
RUN wget -P /usr/local/lib/antlr-4.5.3-complete.jar
http://www.antlr.org/download/antlr-4.5.3-complete.jar && \  
export CLASSPATH=".:/usr/local/lib/antlr-4.5.3-complete.jar:$CLASSPATH" && \  
alias antlr4='java -jar /usr/local/lib/antlr-4.5.3-complete.jar' && \  
alias grun='java org.antlr.v4.gui.TestRig'  

