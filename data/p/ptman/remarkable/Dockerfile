# Copyright (c) 2017 Paul Tötterman <ptman@iki.fi>. All rights reserved.  
FROM debian:sid-slim  
# Author with no obligation to maintain  
MAINTAINER Paul Tötterman <ptman@iki.fi>  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
REMARKABLE_URL="https://remarkable.engineering/remarkable-linux-
client-0.0.5-16-1408-g7eca2b66.tgz"  
  
COPY 00InstallRecommends /etc/apt/apt.conf.d/00InstallRecommends  
RUN apt-get -qq update && \  
apt-get -qq install \  
ca-certificates \  
libkf5archive5 \  
libqt5concurrent5 \  
libqt5quick5 \  
libqt5svg5 \  
libqt5websockets5 \  
libqt5widgets5 \  
libqt5xml5 \  
openssh-server \  
qml-module-qtquick-controls \  
qml-module-qtquick-controls2 \  
qml-module-qtquick-dialogs \  
qml-module-qt-labs-platform \  
qtquickcontrols2-5-dev \  
wget \  
xauth && \  
wget "${REMARKABLE_URL}" -O /remarkable.tgz && \  
tar xzCf /opt /remarkable.tgz && \  
mv /opt/remarkable* /opt/remarkable && \  
rm /remarkable.tgz && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN useradd -s /bin/bash -m -g users remarkable && \  
sed -i -e 's/^\\(remarkable:\\)!:/\1:/' /etc/passwd /etc/shadow && \  
sed -i -e 's/#\\(PermitEmptyPasswords\\) no/\1 yes/' /etc/ssh/sshd_config && \  
sed -i -e 's/@include common-auth/auth sufficient pam_unix.so nullok/'
/etc/pam.d/sshd && \  
mkdir /var/run/sshd && \  
chmod 0755 /var/run/sshd  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["run"]  

