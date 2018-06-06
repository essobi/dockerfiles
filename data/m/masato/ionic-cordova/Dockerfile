FROM phusion/baseimage:0.9.15  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
## Enabling the insecure key permanently  
RUN /usr/sbin/enable_insecure_key  
  
## oracle-java7  
RUN add-apt-repository ppa:webupd8team/java && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
## apt-get update  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y build-essential software-properties-common \  
python emacs24-nox emacs24-el \  
git byobu wget curl unzip tree elinks \  
oracle-java7-installer oracle-java7-set-default ant \  
lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
## Japanese Environment  
ENV LANG ja_JP.UTF-8  
RUN locale-gen $LANG && update-locale $LANG && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
## Development Environment  
RUN update-alternatives --set editor /usr/bin/vim.basic  
  
ENV USERNAME docker  
ENV HOME /home/${USERNAME}  
ENV PATH $PATH:${HOME}/bin  
  
# Add Un-Root User  
RUN useradd -m -d ${HOME} -s /bin/bash ${USERNAME} && \  
echo "${USERNAME}:${USERNAME}" | chpasswd && \  
mkdir ${HOME}/.ssh ${HOME}/tmp && \  
chmod 700 ${HOME}/.ssh && \  
cp /root/.ssh/authorized_keys ${HOME}/.ssh && \  
chmod 600 ${HOME}/.ssh/authorized_keys && \  
chown -R ${USERNAME}:${USERNAME} ${HOME}/.ssh && \  
echo "export LANG=ja_JP.UTF-8" >> ${HOME}/.bashrc && \  
echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
ENV USERNAME docker  
ENV HOME /home/${USERNAME}  
WORKDIR /data  
ENV DATA_DIR /data  
  
ADD dotfiles ${HOME}  
RUN mkdir -p /data && \  
chown -R ${USERNAME}:${USERNAME} ${HOME} ${DATA_DIR}  
  
USER ${USERNAME}  
  
## Cask  
RUN curl -fsSkL https://raw.github.com/cask/cask/master/go | python && \  
echo "export PATH=${HOME}/.cask/bin:$PATH" >> ${HOME}/.profile && \  
/bin/bash -c 'source ${HOME}/.profile && cd ${HOME}/.emacs.d && cask install'  
  
## auto-java-complete  
RUN cd ${HOME}/.emacs.d && \  
git clone https://github.com/emacs-java/auto-java-complete && \  
cd auto-java-complete && \  
javac Tags.java -encoding UTF-8 && \  
java -cp "/usr/lib/jvm/java-7-oracle/jre/lib/rt.jar:." Tags  
  
## Android SDK  
ENV ANDROID_SDK_VERSION r24.0.2  
ENV ANDROID_API_LEVEL 19  
ENV ANDROID_BUILD_TOOLS_VERSION 21.1.1  
ENV ANDROID_HOME ${HOME}/android-sdk-linux  
  
RUN echo "export ANDROID_HOME=${ANDROID_HOME}" >> ${HOME}/.bashrc  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN echo "export PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools" >> ${HOME}/.bashrc  
  
RUN wget -qO- "http://dl.google.com/android/android-
sdk_${ANDROID_SDK_VERSION}-linux.tgz" \  
| tar -zxv -C ${HOME} && \  
echo y | android update sdk --no-ui --all --filter platform-
tool,android-${ANDROID_API_LEVEL},sysimg-${ANDROID_API_LEVEL},build-
tools-${ANDROID_BUILD_TOOLS_VERSION}  
  
ENV NODE_VERSION v0.10  
## Node.js/Cordova/Ionic  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.22.0/install.sh |
bash && \  
/bin/bash -c 'source ${HOME}/.nvm/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias default ${NODE_VERSION} && \  
npm install -g npm && \  
npm install -g cordova ionic && \  
npm install -g ripple-emulator && \  
npm cache clear'  
  
## Create Cordova and ionic sample apps  
RUN /bin/bash -c 'source ${HOME}/.nvm/nvm.sh && nvm use ${NODE_VERSION} \  
cd ${DATA_DIR} && \  
cordova create cordova_test com.example.test "CordovaTestApp" && \  
cd ${DATA_DIR}/cordova_test && \  
cordova platform add android && \  
cordova build && \  
cd ${DATA_DIR} && \  
ionic start ionicTestApp tabs && \  
cd ${DATA_DIR}/ionicTestApp && \  
ionic platform add android && \  
ionic build android'  
  
USER root  
ENV HOME /root  
  
VOLUME ["/data"]  
EXPOSE 8100 35729  
CMD ["/sbin/my_init"]  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

