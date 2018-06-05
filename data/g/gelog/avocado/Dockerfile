# For building this image, See https://github.com/GELOG/docker-ubuntu-spark  
FROM gelog/spark:1.2-bin-hadoop2.3  
# Environment variables  
ENV MAVEN_VERSION 3.2.3  
ENV MAVEN_HOME /usr/local/apache-maven  
ENV MAVEN_OPTS -Xmx512m -XX:MaxPermSize=128m  
ENV AVOCADO_VERSION 0.0.0-master-branch  
ENV AVOCADO_HOME /usr/local/avocado  
ENV PATH $AVOCADO_HOME/bin:$MAVEN_HOME/bin:$PATH  
  
  
# Installing Maven  
RUN wget
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz && \  
tar -xzf /apache-maven-$MAVEN_VERSION-bin.tar.gz -C /usr/local/ && \  
ln -s /usr/local/apache-maven-$MAVEN_VERSION $MAVEN_HOME && \  
rm /apache-maven-$MAVEN_VERSION-bin.tar.gz  
# Verify Maven installation with: mvn -version  
# Installing Avocado  
# FIXME: should pull from official source once the bug is fixed  
RUN wget https://github.com/bigdatagenomics/avocado/archive/master.tar.gz && \  
tar -xzf /master.tar.gz -C /usr/local/ && \  
rm /master.tar.gz && \  
ln -s /usr/local/avocado-master $AVOCADO_HOME && \  
cd $AVOCADO_HOME && \  
mvn package  
  
# FIXME: it takes 25min to build the image  
# FIXME: the virtual image size is 1.07 GB (310 MB for this layer)  
# Default action: print Avocado's options  
CMD ["avocado-submit"]  
  

