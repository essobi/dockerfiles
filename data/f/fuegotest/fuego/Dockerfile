FROM debian:jessie  
MAINTAINER tim.bird@sony.com  
  
#
==============================================================================  
# Prepare basic image  
#
==============================================================================  
ARG DEBIAN_FRONTEND=noninteractive  
  
COPY setup/apt/sources/fuego-debian-jessie.list \  
/etc/apt/sources.list  
RUN apt-get update && \  
apt-get -yV install \  
apt-utils \  
at \  
autoconf \  
automake \  
bc \  
bsdmainutils \  
bzip2 \  
cmake \  
curl \  
daemon \  
diffstat \  
g++ \  
gcc \  
gettext \  
git \  
inotify-tools \  
iperf \  
lava-tool \  
libaio-dev \  
libcairo2-dev \  
libglib2.0-dev \  
libsdl1.2-dev \  
libtool \  
libxmu-dev \  
libxmuu-dev \  
lzop \  
make \  
mc \  
minicom \  
net-tools \  
netcat \  
netperf \  
netpipe-tcp \  
openjdk-7-jdk \  
openjdk-7-jre \  
openssh-server \  
pkg-config \  
python-lxml \  
python-matplotlib \  
python-openpyxl \  
python-paramiko \  
python-parsedatetime \  
python-pip \  
python-requests \  
python-serial \  
python-simplejson \  
python-xmltodict \  
python-yaml \  
rsync \  
sshpass \  
sudo \  
time \  
u-boot-tools \  
vim \  
wget \  
xmlstarlet && \  
apt-get -t jessie-backports install gosu && \  
rm -rf /var/lib/apt/lists/* && \  
echo dash dash/sh boolean false | debconf-set-selections && \  
dpkg-reconfigure dash  
  
RUN pip install \  
filelock \  
python-jenkins==0.4.14  
  
# INFO: Commented out to remove toolchain instala from emdebian, that was
causing conflicts  
# TODO: Move toolchain-related instalation steps to a derivate image, like
fuego:${version}-arhmhf  
# RUN echo deb http://emdebian.org/tools/debian/ jessie main >
/etc/apt/sources.list.d/crosstools.list && \  
# curl http://emdebian.org/tools/debian/emdebian-toolchain-archive.key | apt-
key add - && \  
# dpkg --add-architecture armhf && \  
# apt-get update && \  
# apt-get -yV install \  
# binutils-arm-linux-gnueabihf \  
# cpp-arm-linux-gnueabihf \  
# crossbuild-essential-armhf \  
# gcc-arm-linux-gnueabihf && \  
# rm -rf /var/lib/apt/lists/*  
#
==============================================================================  
# Download and Install Jenkins  
#
==============================================================================  
ARG JENKINS_VERSION=2.32.1  
ARG JENKINS_SHA=bfc226aabe2bb089623772950c4cc13aee613af1  
ARG JENKINS_URL=https://pkg.jenkins.io/debian-
stable/binary/jenkins_${JENKINS_VERSION}_all.deb  
ENV JENKINS_HOME=/var/lib/jenkins  
env JENKINS_CACHE=/var/cache/jenkins  
env JENKINS_LOG=/var/log/jenkins/jenkins.log  
  
ARG uid=1009  
ARG gid=${uid}  
  
RUN echo "Creating Jenkins user/group with uid:gid ${uid}:${gid}"  
  
RUN groupadd -g ${gid} jenkins && \  
useradd -l -d "${JENKINS_HOME}" -u ${uid} -g ${gid} -G sudo -s /bin/bash
jenkins && \  
curl -L -O ${JENKINS_URL} && \  
echo "${JENKINS_SHA} jenkins_${JENKINS_VERSION}_all.deb" | sha1sum -c - && \  
dpkg -i jenkins_${JENKINS_VERSION}_all.deb && \  
rm jenkins_${JENKINS_VERSION}_all.deb  
  
#
==============================================================================  
# Install Fuego Release Test Dependencies  
#
==============================================================================  
# TODO: This session should be moved to a separate Dockerfile in the future,  
# that simply extends a fuego-base image and compiles a Fuego that's capable
of  
# testing itself.  
# Install Dependencies  
RUN apt-get update && \  
apt-get -yV install \  
apt-transport-https \  
ca-certificates \  
chromium \  
curl \  
gnupg2 \  
imagemagick \  
python3 \  
python3-pip \  
python3-pillow \  
software-properties-common && \  
rm -rf /var/lib/apt/lists/* && \  
python3 -m pip install \  
docker \  
pexpect \  
selenium  
  
# Install Docker  
RUN curl -fsSL https://download.docker.com/linux/$(source /etc/os-release; \  
echo "$ID")/gpg | sudo apt-key add - && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(\  
source /etc/os-release; echo "$ID") $(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get -yV install \  
docker-ce  
  
# Install Chrome Driver for SeleniumHQ  
RUN CHROME_DRIVER_VERSION=$(curl --silent --fail \  
https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \  
curl https://chromedriver.storage.googleapis.com/$(\  
echo ${CHROME_DRIVER_VERSION})/chromedriver_linux64.zip \  
-o chrome-driver.zip && \  
unzip chrome-driver.zip -d /usr/local/bin && rm chrome-driver.zip && \  
chmod +x /usr/local/bin/chromedriver  
  
# Setting jenkins as a sudoer. Needed for accessing the dockerd socket.  
RUN echo "jenkins ALL = (root) NOPASSWD:ALL" >> /etc/sudoers  
  
#
==============================================================================  
# Post installation  
#
==============================================================================  
ENV FUEGO_HOME=/var/fuego_home  
ENV RESOURCES=/resources  
  
COPY ./resources ${RESOURCES}  
  
COPY setup/fuego /setup/fuego  
WORKDIR /setup/fuego  
RUN ./setup.sh  
  
COPY setup/jenkins /setup/jenkins  
WORKDIR /setup/jenkins  
RUN ./setup.sh  
  
WORKDIR /setup/jenkins/plugins  
RUN ./install.sh  
  
COPY setup/tools /setup/tools  
WORKDIR /setup  
  
RUN git clone https://github.com/tbird20d/ttc.git /usr/local/src/ttc && \  
./tools/setup-ttc.sh  
  
COPY setup/serial /setup/serial  
RUN git clone https://github.com/frowand/serio.git /usr/local/src/serio && \  
./serial/setup-serio.sh  
  
RUN git clone https://github.com/tbird20d/serlogin.git /usr/local/src/serlogin
&& \  
./serial/setup-serlogin.sh  
  
COPY setup/lava /setup/lava  
RUN ./lava/setup.sh  
  
#
==============================================================================  
# Setup startup command  
#
==============================================================================  
WORKDIR /  
COPY setup/entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

