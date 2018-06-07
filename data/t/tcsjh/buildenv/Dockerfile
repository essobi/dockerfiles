############################################################  
# TCSJOHNHUXLEY GFL Build Image JDK8 #  
############################################################  
FROM ubuntu:16.04  
LABEL maintainer="jessica.mowatt@tcsjohnhuxley.com"  
USER root  
RUN set -x && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y --no-install-recommends openjdk-8-jdk-headless \  
git \  
openssh-client \  
maven \  
unzip \  
curl && \  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get install git-lfs && \  
git lfs install && \  
mkdir -p /home/android/sdk && \  
cd /home/android/sdk && \  
curl -sL https://dl.google.com/android/repository/tools_r25.2.3-linux.zip -o
tools_r25.2.3-linux.zip && \  
unzip tools_r25.2.3-linux.zip && \  
rm tools_r25.2.3-linux.zip && \  
yes | /home/android/sdk/tools/bin/sdkmanager "build-tools;25.0.2" && \  
yes | /home/android/sdk/tools/bin/sdkmanager "platforms;android-17" && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
apt-get purge -y unzip && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
mv /home/android/sdk/tools/source.properties /tmp && \  
rm -rf /home/android/sdk/tools && \  
mkdir /home/android/sdk/tools && \  
mv /tmp/source.properties /home/android/sdk/tools/ && \  
useradd -r -u 1000 -ms /bin/bash builder  
USER builder  

