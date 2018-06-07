############################################################  
# Docker  
#  
############################################################  
  
FROM ifourmanov/nodebuilder:node5  
  
# Environment variables  
# Installing Android SDK  
# Where to download the sdk  
ENV ANDROID_DL_DIR /tmp/sdk  
# Download URL  
ENV ANDROID_SDK_DIST_URL http://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz  
ENV ANDROID_SDK_DIST android-sdk.tgz  
# Android Home Directory  
ENV ANDROID_HOME_ROOT /opt/android-sdk-linux  
# Setting the ANDROID_HOME variable  
ENV ANDROID_HOME $ANDROID_HOME_ROOT/sdk  
# Used Android SDK Versions  
ENV ANDROID_SDK_VERSION_MIN 19  
ENV ANDROID_SDK_VERSION_TARGET 21  
ENV ANDROID_SDK_VERSION_MAX 23  
  
# Installing some system dependencies  
RUN apt-get update && \  
apt-get install -y -q \  
sudo \  
locales \  
default-jdk \  
python \  
g++ \  
git \  
ant \  
make \  
curl \  
ruby-full \  
imagemagick \  
graphicsmagick \  
libmagick++-dev \  
wget \  
ca-certificates \  
expect \  
lib32stdc++6 \  
lib32z1 && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get clean  
  
RUN echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
git config --system url."https://".insteadOf git://  
  
# Locale  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
  
# Setting-up Android SDK  
# Creting the ANDROID_HOME  
RUN mkdir ${ANDROID_HOME_ROOT} && \  
mkdir ${ANDROID_HOME}  
  
  
# Setting the $PATH  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-tools  
  
# Getting the Android SDK  
# Creating the download directory  
RUN mkdir ${ANDROID_DL_DIR} && \  
wget -O ${ANDROID_DL_DIR}/${ANDROID_SDK_DIST} ${ANDROID_SDK_DIST_URL} && \  
tar xzvf ${ANDROID_DL_DIR}/${ANDROID_SDK_DIST} -C ${ANDROID_HOME} --strip-
components=1 && \  
rm -rf ${ANDROID_DL_DIR}  
  
# Updating Android SDK  
RUN echo 'y' | ${ANDROID_HOME}/tools/android update sdk -a -u --filter tools
|| true  
RUN echo 'y' | ${ANDROID_HOME}/tools/android update sdk -a -u --filter
platform-tools || true  
RUN echo 'y' | ${ANDROID_HOME}/tools/android update sdk -a -u --filter build-
tools-23.0.2 || true  
RUN echo 'y' | ${ANDROID_HOME}/tools/android update sdk -a -u --filter
26,27,28,29,30 || true  
  
# Install SASS  
RUN gem install sass  
  
# Cordova  
RUN npm install -g grunt-cli \  
bower \  
cordova \  
plato \  
jscs \  
jshint  
  
# Phantomjs download bug workaround  
ENV PHANTOMJS_CDNURL http://cnpmjs.org/downloads  
  
# Permissions on the ANDROID_ROT and HOME  
ENV BUILDER_FOLDERS ${ANDROID_HOME_ROOT}  

