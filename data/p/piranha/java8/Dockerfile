FROM pallet/ubuntu-nodoc  
MAINTAINER Alexander Solovyov <alexander@solovyov.net>  
  
# Install Java.  
ADD java.sh /opt/  
RUN apt-get install -y curl && /opt/java.sh  
  
ENV JAVA_HOME /opt/java  
ENV JRE_HOME /opt/java/jre  
ENV PATH $PATH:$JAVA_HOME/bin:$JRE_HOME/bin  

