FROM exoplatform/ubuntu-jdk7-exo:plf-4.1  
MAINTAINER Eric Taieb Walch <teknologist@gmail.com>  
  
ENV EXOADDON_SRC_DIR /home/${EXO_USER}/src  
ENV M2_HOME /opt/apache-maven-3.2.5  
# Install Git  
USER root  
  
RUN apt-get -qq update && \  
apt-get -qq -y install git && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y autoclean  
  
#Install Maven 3'  
RUN mkdir -p ${M2_HOME} && \  
curl -L -o /tmp/apache-maven-3.2.5-bin.zip
http://www.us.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.zip && \  
unzip -q /tmp/apache-maven-3.2.5-bin.zip -d /opt/ && \  
rm -f /tmp/apache-maven-3.2.5-bin.zip  
  
USER exo  
  
#Setup Maven for eXo Addons build  
RUN echo 'export M2_HOME=$M2_HOME' >> /home/${EXO_USER}/.bashrc && \  
mkdir /home/${EXO_USER}/.m2 && \  
echo '<settings><mirrors><mirror><id>exo-central-server</id><name>eXo Central
Server</name><url>http://repository.exoplatform.org/public/</url><mirrorOf>central</mirrorOf></mirror></mirrors></settings>'
> /home/${EXO_USER}/.m2/settings.xml && \  
cd /home/${EXO_USER}/.m2 && \  
echo "EXO_JVM_SIZE_MAX=\"3584m\"" > ${EXO_APP_DIR}/current/bin/setenv-
customize.sh && \  
echo "EXO_JVM_SIZE_MIN=\"3584m\"" >> ${EXO_APP_DIR}/current/bin/setenv-
customize.sh  
  
#Clone exo chat addon git / compile the addon to pull dependencies in .m2/ -
cleanup leftovers  
RUN git clone https://github.com/exo-addons/chat-application.git
${EXOADDON_SRC_DIR} && \  
cd ${EXOADDON_SRC_DIR} && ${M2_HOME}/bin/mvn clean package -Dmaven.test.skip
--batch-mode && \  
rm -rf ${EXOADDON_SRC_DIR}  

