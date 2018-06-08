FROM patricol/ubuntu_x11:Cuda  
  
USER root  
  
EXPOSE 8000 8080 9876  
#OpenJDK is already mostly installed in patricol/ubuntu. Uncomment the two
lines below to install and use Oracle Java. Note that both will be in PATH.  
#ENV USE_ORACLE_JAVA=true  
#ENV JAVA_HOME=/usr/lib/jvm/java-$JAVA_MAJOR_VERSION-oracle  
RUN if [ "$USE_ORACLE_JAVA" = "true" ]; \  
then add-apt-repository -y ppa:webupd8team/java && \  
echo "oracle-java$JAVA_MAJOR_VERSION-installer shared/accepted-oracle-
license-v1-1 select true" | debconf-set-selections && \  
apt-get update; \  
apt-get install -y oracle-java$JAVA_MAJOR_VERSION-installer && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*; \  
fi  
  
ENV MAVEN_MAJOR_VERSION=3  
ENV MAVEN_VERSION=$MAVEN_MAJOR_VERSION.5.3  
#Check Maven versions here: https://maven.apache.org/docs/history.html  
ENV M2_HOME=/home/user/apache-maven-$MAVEN_VERSION  
ENV TOMCAT_MAJOR_VERSION=9  
ENV TOMCAT_VERSION=$TOMCAT_MAJOR_VERSION.0.7  
#Check Tomcat versions here: https://archive.apache.org/dist/tomcat/  
ENV TOMCAT_HOME=/home/user/tomcat$TOMCAT_MAJOR_VERSION  
ENV PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH  
  
RUN mkdir $M2_HOME $TOMCAT_HOME && \  
wget -qO- "http://apache.ip-
connect.vn.ua/maven/maven-$MAVEN_MAJOR_VERSION/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C $M2_HOME &&
\  
wget -qO-
"http://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR_VERSION/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz" | tar -zx --strip-components=1 -C $TOMCAT_HOME
&& \  
rm -rf /home/user/tomcat$TOMCAT_MAJOR_VERSION/webapps/* && \  
chown -R user:user $M2_HOME $TOMCAT_HOME  
  
RUN su user -c "umake ide idea /home/user/.local/share/umake/ide/idea" && \  
su user -c "umake ide idea-ultimate /home/user/.local/share/umake/ide/idea-
ultimate"  
  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
RUN chown -R user:user /home/user/.config/  
  
USER user

