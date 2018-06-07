FROM eclairiuss/java  
  
ENV MAVEN_HOME /usr/share/maven  
  
ARG MAVEN_VERSION=3.3.9  
ARG USER_HOME_DIR="/root"  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
WORKDIR /tmp  
  
RUN mkdir -p $MAVEN_HOME/ref && \  
wget ${BASE_URL}/apache-maven-$MAVEN_VERSION-bin.tar.gz && \  
tar -xzf apache-maven-$MAVEN_VERSION-bin.tar.gz -C /usr/share/maven --strip-
components=1 && \  
rm -f apache-maven-$MAVEN_VERSION-bin.tar.gz && \  
ln -s $MAVEN_HOME/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
WORKDIR /  
  
COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh  
COPY settings-docker.xml $MAVEN_HOME/ref/  
  
RUN chmod 755 /usr/local/bin/mvn-entrypoint.sh  
  
VOLUME "$USER_HOME_DIR/.m2"  
  
ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]  
CMD ["mvn"]

