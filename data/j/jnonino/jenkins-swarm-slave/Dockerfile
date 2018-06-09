FROM openjdk:8-jdk  
LABEL maintainer="Julian Nonino <noninojulian@outlook.com>"  
  
# Update the system  
RUN apt-get update -y && \  
apt-get install -y git subversion mercurial wget curl tzdata unzip xz-utils
build-essential libssl-dev ruby ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Gradle  
ENV GRADLE_VERSION 4.5.1  
RUN echo "Install Gradle" && \  
wget https://downloads.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip
&& \  
unzip gradle-$GRADLE_VERSION-bin.zip && \  
mv gradle-$GRADLE_VERSION /opt/gradle && \  
rm -rf gradle-$GRADLE_VERSION-bin.zip  
ENV GRADLE_HOME /opt/gradle  
ENV PATH $GRADLE_HOME/bin:$PATH  
  
# Install Maven  
ENV MAVEN_VERSION 3.5.2  
RUN echo "Install Maven" && \  
wget
http://mirrors.dcarsat.com.ar/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz && \  
tar -zxf apache-maven-$MAVEN_VERSION-bin.tar.gz && \  
mv apache-maven-$MAVEN_VERSION /opt/maven && \  
rm -rf apache-maven-$MAVEN_VERSION-bin.tar.gz  
ENV MAVEN_HOME /opt/maven  
ENV PATH $MAVEN_HOME/bin:$PATH  
  
# Install Ant  
ENV ANT_VERSION 1.10.2  
RUN echo "Install Ant" && \  
wget https://www.apache.org/dist/ant/binaries/apache-ant-$ANT_VERSION-
bin.tar.gz && \  
tar -zxf apache-ant-$ANT_VERSION-bin.tar.gz && \  
mv apache-ant-$ANT_VERSION /opt/ant && \  
rm -rf apache-ant-$ANT_VERSION-bin.tar.gz  
ENV ANT_HOME /opt/ant  
ENV PATH $ANT_HOME/bin:$PATH  
  
# Install Python  
ENV PYTHON_VERSION 2.7.14  
ENV PYTHON_PIP_VERSION 9.0.1  
RUN apt-get update && \  
apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev
libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev && \  
wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
&& \  
mkdir -p /usr/src/python && \  
tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz && \  
rm python.tar.xz && \  
cd /usr/src/python && \  
./configure --enable-shared --enable-unicode=ucs4 && \  
make && \  
make install && \  
ldconfig && \  
wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' && \  
python2 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" && \  
rm /tmp/get-pip.py && \  
pip install --no-cache-dir --upgrade --force-reinstall
"pip==$PYTHON_PIP_VERSION" && \  
rm -rf /usr/src/python ~/.cache  
COPY pip_requirements.txt /usr/local/bin/pip_requirements.txt  
RUN pip install -r /usr/local/bin/pip_requirements.txt  
  
# Install Node.js  
ENV NODEJS_VERSION 8.9.3  
RUN wget https://nodejs.org/dist/v$NODEJS_VERSION/node-v$NODEJS_VERSION-
linux-x64.tar.xz && \  
tar -xJf node-v$NODEJS_VERSION-linux-x64.tar.xz -C /usr/local \--strip-
components=1 && \  
rm node-v$NODEJS_VERSION-linux-x64.tar.xz  
  
# Install Sonar Runner  
ENV SONAR_RUNNER_VERSION 2.4  
RUN echo "Install Sonar Runner" && \  
wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-
dist/$SONAR_RUNNER_VERSION/sonar-runner-dist-$SONAR_RUNNER_VERSION.zip && \  
unzip sonar-runner-dist-$SONAR_RUNNER_VERSION.zip && \  
mv sonar-runner-$SONAR_RUNNER_VERSION /opt/sonar-runner && \  
rm -rf sonar-runner-dist-$SONAR_RUNNER_VERSION.zip && \  
rm -rf /opt/sonar-runner/conf/sonar-runner.properties  
ENV SONAR_RUNNER_HOME /opt/sonar-runner  
ENV PATH $SONAR_RUNNER_HOME/bin:$PATH  
  
# Add Jenkins Slave user and add it to sudoers and create .m2 folder the user  
RUN useradd -c "Jenkins Slave user" -d /home/jenkins-slave -m jenkins-slave &&
\  
echo "jenkins-slave ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# Create Maven .m2 folder  
RUN mkdir /home/jenkins-slave/.m2 && \  
mkdir /home/jenkins-slave/.m2/repository && \  
chown -R jenkins-slave:jenkins-slave /home/jenkins-slave/.m2  
  
# Copy Start script  
COPY start_slave.sh /usr/local/bin/start_slave.sh  
  
# Download Jenkins Swarm and condigure  
ENV JENKINS_SWARM_VERSION 3.4  
RUN curl --create-dirs -sSLo /usr/share/jenkins/swarm-client-jar-with-
dependencies.jar https://repo.jenkins-ci.org/releases/org/jenkins-
ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-
client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar && \  
chmod 755 /usr/share/jenkins && \  
chmod +x /usr/local/bin/start_slave.sh  
  
# Switch to Jenkins Slave user  
USER jenkins-slave  
  
# Copying default Maven Settings  
COPY settings.xml /home/jenkins-slave/.m2/settings.xml  
  
#Entrypoint  
ENTRYPOINT ["/usr/local/bin/start_slave.sh"]  

