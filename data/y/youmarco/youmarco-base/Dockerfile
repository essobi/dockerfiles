FROM fedora:latest  
  
RUN echo "deltarpm=0" >> /etc/dnf/dnf.conf \  
&& dnf update -y \  
&& curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - \  
&& dnf install -y \  
xorg-x11-server-Xvfb \  
firefox \  
java-1.8.0-openjdk-headless \  
lsof \  
nodejs \  
gcc-c++ \  
make \  
tar \  
bzip2 \  
which \  
git \  
&& npm install -g grunt-cli node-gyp phantomjs-prebuilt\  
&& node-gyp install \  
&& pip install --upgrade pip setuptools markerlib \  
&& dnf clean all \  
&& dbus-uuidgen > /var/lib/dbus/machine-id  
  
ENV GCLOUD_SDK_VERSION 118.0.0  
ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-$GCLOUD_SDK_VERSION-linux-x86_64.tar.gz google-cloud-sdk.tar.gz  
RUN tar -C /srv -xf google-cloud-sdk.tar.gz && \  
/srv/google-cloud-sdk/install.sh \  
\--path-update true \  
\--command-completion true \  
\--additional-components app-engine-python \  
\--quiet && \  
rm -f google-cloud-sdk.tar.gz  
  
ENV HOME=/tmp  
ENV PATH=$PATH:/srv/google-cloud-sdk/bin  

