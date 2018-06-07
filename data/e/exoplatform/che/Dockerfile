# Docker image for eXo Platform and Che development.  
#  
FROM exoplatform/exo-community:4.3  
MAINTAINER GREAU Maxime <mgreau+docker@exoplatform.com>  
  
USER root  
  
ENV LANG C.UTF-8  
# URL used to download configuration files  
ENV EXO_CHE_CONF_URL https://raw.githubusercontent.com/exo-docker/exo-
che/master/base-che  
  
ENV MAVEN_VERSION=3.2.5  
ENV M2_HOME=/home/${EXO_USER}/apache-maven-$MAVEN_VERSION  
ENV PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH  
  
# Install Git (required tool for Che)  
RUN add-apt-repository ppa:git-core/ppa && \  
apt-get update && \  
sudo apt-get install git -y && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Maven  
RUN mkdir /home/${EXO_USER}/apache-maven-$MAVEN_VERSION && \  
wget -qO- "http://apache.ip-
connect.vn.ua/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C
/home/exo/apache-maven-$MAVEN_VERSION/  
RUN echo "export JAVA_HOME=$JAVA_HOME\nexport M2_HOME=/home/exo/apache-
maven-$MAVEN_VERSION\nexport PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH" >>
/home/exo/.bashrc  
  
# Add eXo Custom Maven settings.xml and exo.properties  
RUN mkdir -p /home/${EXO_USER}/.m2/repository && chown ${EXO_USER}:${EXO_USER}
/home/${EXO_USER}/.m2/repository && \  
curl -L -o /home/${EXO_USER}/.m2/settings.xml
${EXO_CHE_CONF_URL}/m2-settings.xml && \  
chown ${EXO_USER}:${EXO_USER} /home/${EXO_USER}/.m2/settings.xml && \  
curl -L -o ${EXO_CONF_DIR}/exo.properties ${EXO_CHE_CONF_URL}/exo-
sample.properties && \  
chown ${EXO_USER}:${EXO_USER} ${EXO_CONF_DIR}/exo.properties  
  
USER ${EXO_USER}  
  
# Init .m2 local repository with artifacts used for PLF and Add-ons
developement  
RUN git clone https://github.com/exoplatform/task.git /home/${EXO_USER}/tmp &&
\  
mvn -f /home/${EXO_USER}/tmp/ install -DskipTests && \  
for x in `find "/home/${EXO_USER}/.m2/repository" -name '*-SNAPSHOT*'`; do rm
-rf "$x"; done && \  
rm -rf /home/${EXO_USER}/tmp  
  
EXPOSE 4403 8000 8080 9876 22  
# CMD for Che Server  
CMD sudo /usr/sbin/sshd -D && \  
tail -f /dev/null  

