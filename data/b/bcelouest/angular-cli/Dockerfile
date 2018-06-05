FROM ubuntu:trusty  
MAINTAINER TIMWI <contact@timwi.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
NODE_VERSION=8.2.1 \  
MAVEN_VERSION=3.5.0 \  
SONAR_SCANNER=3.0.0.702-linux \  
SONAR_URL=http://localhost:9000 \  
DISPLAY=":1"  
# Set the timezone  
RUN sudo echo "Europe/Paris" > /etc/timezone  
RUN sudo dpkg-reconfigure -f noninteractive tzdata  
  
# Setup environment  
ENV PATH ${PATH}:/opt/sonar-scanner/bin:/opt/nsis-2.46/bin:/opt/gradle-3.5/bin  
  
# Install basics  
RUN apt-get update && \  
apt-get install -y git wget curl unzip bzip2 libfontconfig build-essential
python python-dev sshpass  
  
# Install node  
RUN curl --retry 3 -SLO
"http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
&& \  
tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 && \  
rm "node-v$NODE_VERSION-linux-x64.tar.gz"  
  
RUN mkdir xnet  
  
# install python-software-properties (so you can do add-apt-repository)  
RUN apt-get update && apt-get install -y -q python-software-properties
software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get -y install oracle-java8-installer  
  
# Install Google Chrome Browser  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get update -qqy && \  
apt-get -qqy install google-chrome-stable && \  
rm /etc/apt/sources.list.d/google-chrome.list && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Sonarqube scanner  
RUN wget -q https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/sonar-scanner-cli-${SONAR_SCANNER}.zip && \  
unzip sonar-scanner-cli-${SONAR_SCANNER}.zip -d /opt && \  
rm sonar-scanner-cli-${SONAR_SCANNER}.zip && \  
mv /opt/sonar-scanner-${SONAR_SCANNER} /opt/sonar-scanner && \  
sed -i "s|#sonar.host.url=\\(.*\\)$|sonar.host.url=$SONAR_URL|" /opt/sonar-
scanner/conf/sonar-scanner.properties  
  
# Install Maven (for war packaging)  
ARG
BASE_URL=https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries  
#http://apache.crihan.fr/dist/maven/maven-3/${MAVEN_VERSION}/binaries  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# Add xnet user  
RUN useradd -ms /bin/bash xnet && \  
echo 'xnet ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
chown -Rf xnet xnet && \  
echo 'PATH=${PATH}:/opt/sonar-scanner/bin\n' > /home/xnet/.bashrc && \  
echo 'export PATH' >> /home/xnet/.bashrc && \  
chmod +x /opt/sonar-scanner/bin/sonar-scanner  
  
RUN echo "xnet ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/xnet  
  
COPY npmrc /home/xnet/.npmrc  
RUN chown xnet /home/xnet/.npmrc  
  
USER xnet  
WORKDIR /home/xnet  
  
ENV MAVEN_HOME /usr/share/maven  
  
RUN mkdir .m2  
RUN git clone https://bitbucket.org/bceclouest/docker-mvn-conf.git /tmp/mvn-
conf && \  
mv /tmp/mvn-conf/settings.xml .m2/ && \  
rm -rf /tmp/mvn-conf/  
  
ADD bashrc .  
RUN cat bashrc >> .bashrc && rm bashrc  
  
EXPOSE 4200  
EXPOSE 49152  
EXPOSE 8100  
ENTRYPOINT bash  
  

