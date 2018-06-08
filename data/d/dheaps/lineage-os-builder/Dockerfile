FROM ubuntu:latest  
  
VOLUME /home/lineage/android/lineage /opt/lineage-os/repo  
VOLUME /home/lineage/.ccache /opt/lineage-os/ccache  
  
#Install system dependencies  
RUN apt-get update -qq && \  
apt-get install -y locales tzdata && \  
# chfn workaround - Known issue within Dockers  
ln -s -f /bin/true /usr/bin/chfn && \  
# set the locale  
locale-gen en_US.UTF-8 && \  
# prepare apt  
apt-get install -y software-properties-common --no-install-recommends && \  
add-apt-repository ppa:openjdk-r/ppa -y && \  
apt-get update && \  
# Install common build tools and java  
apt-get install -y bc bison build-essential ccache curl flex g++-multilib gcc-
multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev
lib32z1-dev libesd0-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev
libwxgtk3.0-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-
tools xsltproc zip zlib1g-dev openjdk-8-jdk && \  
apt-get install -y wget --no-install-recommends && \  
# clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true )) && \  
# Add Lineage user  
useradd -c 'Lineage OS Builder' -u 1000 -g 100 -m -d /home/lineage -s
/bin/bash lineage && \  
chown -R lineage:users /home/lineage/  
USER lineage  
# Install Android build tools  
RUN mkdir -p /home/lineage/bin && \  
mkdir -p /home/lineage/android/lineage && \  
curl https://storage.googleapis.com/git-repo-downloads/repo >
/home/lineage/bin/repo && \  
chmod a+x /home/lineage/bin/repo && \  
cd /home/lineage/android && \  
wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
&& \  
unzip platform-tools-latest-linux.zip && \  
rm platform-tools-latest-linux.zip  
  
ENV USE_CCACHE=1  
ENV PATH "$PATH:/home/lineage/bin:/home/lineage/android/platform-tools"  
ENV ANDROID_JACK_VM_ARGS="-Dfile.encoding=UTF-8 -XX:+TieredCompilation -Xmx4G"  
  
ENTRYPOINT /bin/bash

