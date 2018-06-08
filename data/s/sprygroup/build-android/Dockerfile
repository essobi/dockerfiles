FROM greyfoxit/alpine-openjdk8:8u131  
  
# maintainer: Greyfox Team | team@greyfox.it | @greyfoxit  
  
# Setup  
  
ENV VERSION_SDK_TOOLS=3952940 \  
ANDROID_HOME=/usr/local/android-sdk-linux  
  
ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools  
  
RUN mkdir -p $ANDROID_HOME && \  
chown -R root.root $ANDROID_HOME && \  
  
# Install dependencies  
  
apk add --no-cache bash curl git openssl openssh-client ca-certificates && \  
  
# Install Android SDK  
  
wget -q -O sdk.zip http://dl.google.com/android/repository/sdk-tools-
linux-$VERSION_SDK_TOOLS.zip && \  
unzip sdk.zip -d $ANDROID_HOME && \  
rm -f sdk.zip && \  
  
# Install licenses  
  
mkdir -p $ANDROID_HOME/licenses/ && \  
echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
$ANDROID_HOME/licenses/android-sdk-license && \  
echo "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
# Install and update Android packages  
  
ADD packages.txt $ANDROID_HOME  
RUN mkdir -p /root/.android && \  
touch /root/.android/repositories.cfg && \  
  
$ANDROID_HOME/tools/bin/sdkmanager --update && \  
(while [ 1 ]; do sleep 5; echo y; done) | $ANDROID_HOME/tools/bin/sdkmanager
--package_file=$ANDROID_HOME/packages.txt  

