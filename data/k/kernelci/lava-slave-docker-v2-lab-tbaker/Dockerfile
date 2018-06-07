FROM bitnami/minideb:unstable  
  
# Add services helper utilities to start and stop LAVA  
COPY scripts/stop.sh .  
COPY scripts/start.sh .  
  
RUN \  
echo 'lava-server lava-server/instance-name string lava-slave-instance' |
debconf-set-selections && \  
echo 'locales locales/locales_to_be_generated multiselect C.UTF-8 UTF-8,
en_US.UTF-8 UTF-8 ' | debconf-set-selections && \  
echo 'locales locales/default_environment_locale select en_US.UTF-8' |
debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive install_packages \  
locales \  
lava-dispatcher \  
lava-dev \  
git \  
vim \  
sudo \  
expect \  
u-boot-tools \  
python-setproctitle \  
device-tree-compiler \  
qemu-system \  
qemu-system-arm \  
qemu-system-i386 \  
qemu-kvm \  
e2fsprogs \  
android-tools-fastboot \  
android-tools-adb \  
android-tools-fsutils \  
tftpd-hpa \  
apache2 \  
ser2net \  
dfu-util \  
libusb-1.0-0-dev \  
libudev-dev \  
python-dev \  
python-pip  
  
RUN \  
pip install setuptools wheel --upgrade && \  
pip install --pre -U pyocd  
  
RUN \  
git clone -b master https://github.com/EmbeddedAndroid/lava-dispatcher.git
/root/lava-dispatcher && \  
cd /root/lava-dispatcher && \  
git checkout release && \  
git config --global user.name "Docker Build" && \  
git config --global user.email "info@kernelci.org" && \  
echo "cd \${DIR} && dpkg -i *.deb" >> /usr/share/lava-server/debian-dev-
build.sh && \  
sed -i 's,dch -v ${VERSION}-1 -D unstable "Local developer build",dch -v
${VERSION}-1 -b -D unstable "Local developer build",g' /usr/share/lava-
server/debian-dev-build.sh && \  
sleep 2 && \  
/usr/share/lava-server/debian-dev-build.sh -p lava-dispatcher  
  
RUN \  
cd /root && \  
git clone https://github.com/Yepkit/pykush && \  
cd pykush/ && \  
python setup.py install  
  
RUN \  
cp /usr/share/lava-dispatcher/apache2/lava-dispatcher.conf /etc/apache2/sites-
available/lava-dispatcher.conf && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2dissite 000-default && \  
a2ensite lava-dispatcher  
  
RUN mkdir -p /etc/lava-coordinator  
  
COPY configs/lava-coordinator.conf /etc/lava-coordinator/lava-coordinator.conf  
  
COPY configs/lava-slave /etc/lava-dispatcher/lava-slave  
  
COPY configs/tftpd-hpa /etc/default/tftpd-hpa  
  
COPY configs/ser2net.conf /etc/ser2net.conf  
  
COPY scripts/ /root/scripts  
  
RUN chmod a+x /root/scripts/*  
  
EXPOSE 69/udp  
  
CMD /start.sh && bash  

