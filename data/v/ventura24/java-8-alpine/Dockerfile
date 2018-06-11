FROM anapsix/alpine-java:jre8  
MAINTAINER ventura24  
  
ENV JAVA_VER 8  
ENV JAVA_HOME /opt/jdk  
  
ADD jce/jce_policy-8.zip /tmp/jce_policy-8.zip  
RUN unzip /tmp/jce_policy-8.zip -d . && \  
cp -v UnlimitedJCEPolicyJDK8/*.jar $JAVA_HOME/jre/lib/security && \  
rm /tmp/jce_policy-8.zip && \  
rm -rf UnlimitedJCEPolicyJDK8  
  
  
  

