FROM openjdk:8u141-jdk  
  
LABEL maintainer1="Jonathan Bergen <jonathan.bergen@fromatob.com>" \  
maintainer2="Roberto Estivill <roberto.estivill@fromatob.com>"  
  
####################  
# Install utils  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y -qq --no-install-recommends \  
curl \  
gcc \  
gzip \  
openssh-client \  
python \  
python-dev \  
python-setuptools \  
python-pip \  
tar \  
wget \  
zip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
pip install -U crcmod  
  
####################  
# Gcloud  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& \  
unzip google-cloud-sdk.zip && \  
rm google-cloud-sdk.zip && \  
google-cloud-sdk/install.sh \  
\--usage-reporting=false \  
\--path-update=true \  
\--bash-completion=false \  
\--additional-components alpha beta  
  
###################  
# Android  
ENV ANDROID_HOME="/opt/android"  
# Download and extract Android Tools  
# https://developer.android.com/studio/index.html#command-tools  
RUN wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
-O /tmp/android-tools.zip && \  
mkdir -p ${ANDROID_HOME} && \  
mkdir -p ${ANDROID_HOME}/licenses/ && \  
unzip /tmp/android-tools.zip -d ${ANDROID_HOME} && \  
rm -rfv /tmp/android-tools.zip && \  
rm -rfv ${ANDROID_HOME}/tools/lib/monitor*  
  
###################  
# Dex count utility  
ENV DEX_COUNT_HOME="/opt/dex-count"  
RUN git clone \--depth 1 https://github.com/mihaip/dex-method-counts.git
${DEX_COUNT_HOME} && \  
cd ${DEX_COUNT_HOME} && \  
./gradlew assemble && \  
rm -rf /root/.gradle  
  
###################  
# PATH  
ENV PATH "$PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:/google-cloud-
sdk/bin/:${DEX_COUNT_HOME}/"  

