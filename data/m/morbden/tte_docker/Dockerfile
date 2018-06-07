FROM eclipse/ubuntu_jdk8  
  
EXPOSE 22 3000 4403 5000 6080 8000 8080 9000  
# Sming ENV  
ENV SMING_BASE=/home/user/sming  
  
ENV ESP_HOME=$SMING_BASE/esp-open-sdk  
ENV SMING_HOME=$SMING_BASE/Sming/Sming  
  
# Nodejs ENV  
ENV NODE_VERSION=9.9.0 \  
NODE_PATH=/usr/local/lib/node_modules  
  
# Python ENV  
ENV GAE=/home/user/google_appengine  
  
# Android ENV  
ENV ANDROID_HOME=/home/user/android-sdk-linux  
  
# PATH  
ENV PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$ESP_HOME/esptool2:$PATH  
  
# Install all dependencies  
RUN sudo apt-get update && \  
sudo apt-get install \  
g++ \  
gcc \  
make \  
gdb \  
gdbserver \  
unrar \  
autoconf \  
automake \  
libtool \  
libtool-bin \  
gperf \  
flex \  
bison \  
texinfo \  
gawk \  
ncurses-dev \  
libexpat1-dev \  
python \  
sed \  
python-serial \  
python-dev \  
srecord \  
bc \  
git \  
help2man \  
unzip \  
build-essential \  
libssl-dev \  
libkrb5-dev \  
ruby-full \  
rubygems-integration \  
-y && \  
sudo apt-get clean && \  
sudo apt-get -y autoremove && \  
sudo rm -rf /var/lib/apt/lists/*  
  
# Sming RUN  
RUN mkdir -p $SMING_BASE && \  
cd $SMING_BASE && \  
git clone \--recursive https://github.com/pfalcon/esp-open-sdk.git && \  
cd $ESP_HOME && \  
sudo chmod 777 -R && \  
make VENDOR_SDK=1.5.4 STANDALONE=y && \  
git clone git clone https://github.com/raburton/esptool2 && \  
cd $ESP_HOME/esptool2 && \  
make  
  
RUN cd $SMING_HOME/../.. && \  
git clone https://github.com/SmingHub/Sming.git && \  
cd Sming && \  
git checkout origin/master && \  
cd Sming && \  
make ENABLE_SSH=true  
  
# Nodejs RUN  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done && \  
cd /home/user && curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
\  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep "node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& sudo tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local
\--strip-components=1 \  
&& sudo rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
RUN sudo npm install -g npm@latest  
RUN sudo npm install --unsafe-perm -g gulp bower grunt grunt-cli yeoman-
generator yo generator-angular generator-karma generator-webapp  
  
# Python RUN  
RUN sudo apt-get update && \  
sudo apt-get install --no-install-recommends -y -q build-essential python2.7
python2.7-dev python-pip && \  
sudo pip install -U pip && \  
sudo pip install virtualenv  
RUN wget -qO- "https://storage.googleapis.com/appengine-
sdks/featured/google_appengine_1.9.40.zip" -O /tmp/gae-sdk.zip && \  
unzip -q /tmp/gae-sdk.zip -d /home/user && \  
rm /tmp/gae-sdk.zip  
  
# Android RUN  
LABEL che:server:6080:ref=VNC che:server:6080:protocol=http  
  
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
useradd -u 1000 -G users,sudo -d /home/user --shell /bin/bash -m user && \  
echo "secret\nsecret" | passwd user  
  
USER user  
RUN sudo dpkg --add-architecture i386 && \  
sudo apt-get update && sudo apt-get install -y --force-yes expect libswt-
gtk-3-java lib32z1 lib32ncurses5 lib32stdc++6 supervisor x11vnc xvfb net-tools
\  
blackbox rxvt-unicode xfonts-terminus sudo openssh-server procps \  
wget unzip mc curl software-properties-common python-software-properties && \  
sudo mkdir /var/run/sshd && \  
sudo sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
sudo add-apt-repository ppa:git-core/ppa && \  
sudo apt-get update && \  
sudo sudo apt-get install git subversion -y && \  
mkdir /home/user/apache-maven-$MAVEN_VERSION && \  
wget \  
\--no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
-qO- \  
"http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-b14/jdk-$JAVA_VERSION-linux-x64.tar.gz" | sudo tar
-zx -C /opt/ && \  
wget -qO-
"https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C
/home/user/apache-maven-$MAVEN_VERSION/ && \  
cd /home/user && wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && tar -xvf
android-sdk.tgz && rm android-sdk.tgz && \  
sudo apt-get clean && \  
sudo apt-get -y autoremove && \  
sudo rm -rf /var/lib/apt/lists/* && \  
echo y | android update sdk --all --force --no-ui --filter platform-
tools,build-tools-21.1.1,android-21,sys-img-armeabi-v7a-android-21 && \  
echo "no" | android create avd \  
\--name che \  
\--target android-21 \  
\--abi armeabi-v7a && \  
sudo mkdir -p /opt/noVNC/utils/websockify && \  
wget -qO- "http://github.com/kanaka/noVNC/tarball/master" | sudo tar -zx
--strip-components=1 -C /opt/noVNC && \  
wget -qO- "https://github.com/kanaka/websockify/tarball/master" | sudo tar -zx
--strip-components=1 -C /opt/noVNC/utils/websockify && \  
sudo mkdir -p /etc/X11/blackbox && \  
echo "[begin] (Blackbox) \n [exec] (Terminal) {urxvt -fn
"xft:Terminus:size=12"} \n \  
[exec] (Emulator) {emulator64-arm -avd che} \n \  
[end]" | sudo tee -a /etc/X11/blackbox/blackbox-menu && \  
echo "#! /bin/bash\n set -e\n sudo /usr/sbin/sshd -D &\n/usr/bin/supervisord
-c /opt/supervisord.conf &\n exec \"\$@\"" > /home/user/entrypoint.sh && chmod
a+x /home/user/entrypoint.sh  
  
ADD index.html /opt/noVNC/  
ADD supervisord.conf /opt/  
RUN svn --version && \  
sed -i 's/# store-passwords = no/store-passwords = yes/g'
/home/user/.subversion/servers && \  
sed -i 's/# store-plaintext-passwords = no/store-plaintext-passwords = yes/g'
/home/user/.subversion/servers  
ENTRYPOINT ["/home/user/entrypoint.sh"]  
  
WORKDIR /projects  
  
CMD tail -f /dev/null  

