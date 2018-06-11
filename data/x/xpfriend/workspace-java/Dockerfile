FROM xpfriend/workspace-base:3.29.0  
MAINTAINER ototadana@gmail.com  
  
ENV MVN_VERSION 3.3.9  
RUN wget
http://www.us.apache.org/dist/maven/maven-3/${MVN_VERSION}/binaries/apache-
maven-${MVN_VERSION}-bin.zip -P /tmp \  
&& unzip /tmp/apache-maven-${MVN_VERSION}-bin.zip -d ~ \  
&& rm -f /tmp/apache-maven-${MVN_VERSION}-bin.zip  
  
ENV M2_HOME ${WORKSPACE}/apache-maven-${MVN_VERSION}  
ENV M2 ${M2_HOME}/bin  
ENV PATH ${M2}:${PATH}  
RUN echo "PATH=${PATH};export PATH" |sudo tee /etc/profile.d/mvn.sh  
  
COPY ./config/. /config/  
RUN sudo chown -R owner:owner /config  
RUN chmod +x /config/*  

