FROM anapsix/alpine-java:jre7  
MAINTAINER ventura24  
  
ENV JAVA_VER 7  
ENV JAVA_HOME /opt/jdk  
  
ADD jce/UnlimitedJCEPolicyJDK7.zip /tmp/UnlimitedJCEPolicyJDK7.zip  
RUN unzip /tmp/UnlimitedJCEPolicyJDK7.zip -d . && \  
cp -v UnlimitedJCEPolicy/*.jar $JAVA_HOME/jre/lib/security && \  
rm /tmp/UnlimitedJCEPolicyJDK7.zip && \  
rm -rf UnlimitedJCEPolicy  
  
  
  

