FROM dnoliver/upm-base  
  
# Update apt-get  
RUN apt-get -y update && apt-get -y --no-install-recommends install \  
# Python 2 Build Dependencies  
python python-dev python-pip python-mraa \  
# Python 3 Build Dependencies  
python3 python3-dev python3-pip python3-mraa \  
# Docs Build Dependencies  
python-sphinx  
  
# Install Python Test Dependencies  
RUN pip install chardet && pip3 install chardet  
  
# Install virtualenv  
RUN pip install virtualenv  
  
# Update apt-get  
RUN apt-get -y update && \  
# Java Build Dependencies  
apt-get -y --no-install-recommends install \  
default-jre default-jdk libmraa-java  
  
# Configure Java Home  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
# RPM Build Dependencies  
RUN apt-get -y update && apt-get -y --no-install-recommends install rpm  
  
WORKDIR /opt  
  
# IPK Build Dependencies  
RUN git clone \--depth=1 https://git.yoctoproject.org/git/opkg-utils  
ENV PATH /opt/opkg-utils:$PATH  
  
# Node.js Build Dependencies  
ARG NVM_VERSION=v0.33.2  
RUN wget -q -O -
https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh |
bash  
ENV NVM_DIR /root/.nvm  
ARG NODE_VERSION  
RUN . $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use $NODE_VERSION &&
\  
npm install -g node-gyp yuidocjs && \  
node-gyp install  
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH  
  
# Static Code Analysis Scanner  
ENV SONAR_DIR /opt/sonar  
ENV SONAR_VER "3.0.3.778"  
WORKDIR $SONAR_DIR  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_VER}-linux.zip && \  
wget https://sonarqube.com/static/cpp/build-wrapper-linux-x86.zip && \  
unzip sonar-scanner-cli-${SONAR_VER}-linux.zip && \  
unzip build-wrapper-linux-x86.zip && \  
rm sonar-scanner-cli-${SONAR_VER}-linux.zip build-wrapper-linux-x86.zip  
ENV PATH $SONAR_DIR/sonar-scanner-${SONAR_VER}-linux/bin:$SONAR_DIR/build-
wrapper-linux-x86:$PATH  
  
# Set Workdir  
WORKDIR $UPM_SRC_DIR  
  
CMD bash  

