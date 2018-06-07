# QEMU/KVM  
# VERSION 0.3  
FROM ceph/daemon  
MAINTAINER d.p.karpov@gmail.com  
  
ENV QEMU_VERSION 2.9.0  
  
ENV PROCWRAPPER_VER 0.0.3  
ENV PY_ETCD_VER 0.4.2  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD qmp-shell /qmp-shell  
ADD qemu-ga-client /qemu-ga-client  
  
RUN buildDeps=' \  
gcc \  
git \  
make \  
python-pip \  
python3-pip \  
python3-setuptools \  
python-setuptools \  
python3-dev \  
libffi-dev \  
libssl-dev \  
pkg-config \  
libglib2.0-dev \  
libfdt-dev \  
libpixman-1-dev \  
zlib1g-dev \  
liblzo2-dev \  
libsnappy-dev \  
libbz2-dev \  
uuid-dev \  
libaio-dev \  
libspice-protocol-dev libspice-server-dev \  
libusb-1.0-0-dev \  
librbd-dev \  
libattr1-dev \  
libcap-dev \  
' \  
set -x && \  
echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
sed -i 's/archive.ubuntu.com/ru.archive.ubuntu.com/g' /etc/apt/sources.list &&
\  
apt-get update && apt-get -y install --no-install-recommends $buildDeps \  
python3-urllib3 \  
libpixman-1-0 \  
libspice-server1 \  
libusb-1.0-0 \  
libfdt1 \  
curl && \  
pip3 install -e git+https://github.com/jplana/python-
etcd.git@${PY_ETCD_VER}#egg=etcd && \  
pip install -e git+https://github.com/jplana/python-
etcd.git@${PY_ETCD_VER}#egg=etcd && \  
pip3 install -e git+https://bitbucket.org/dmitry_karpov/python-
procwrapper.git@${PROCWRAPPER_VER}#egg=procwrapper && \  
pip3 install -e git+https://bitbucket.org/dmitry_karpov/python-qmp.git#egg=qmp
&& \  
pip install -e git+https://bitbucket.org/dmitry_karpov/python-qmp.git#egg=qmp
&& \  
wget http://wiki.qemu.org/download/qemu-${QEMU_VERSION}.tar.bz2 && \  
tar -xf qemu-${QEMU_VERSION}.tar.bz2 && \  
cd qemu-${QEMU_VERSION} && \  
./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--docdir=/usr/share/doc/qemu-${QEMU_VERSION} \  
\--target-list=x86_64-softmmu \  
\--enable-rbd \  
\--enable-linux-aio \  
\--enable-libusb \  
\--enable-lzo \  
\--enable-snappy \  
\--enable-bzip2 \  
\--enable-guest-agent \  
\--enable-vhdx \  
\--enable-uuid \  
\--enable-virtfs \  
\--enable-spice && \  
make && make install && \  
cd .. && \  
rm -rf qemu-${QEMU_VERSION}* && \  
ln -s /usr/bin/qemu-system-x86_64 /usr/bin/kvm && \  
apt-get -y purge --auto-remove $buildDeps && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN chmod +x \  
/qmp-shell \  
/qemu-ga-client \  
&& mkdir -p /iso  
  
RUN curl -sSL https://fedorapeople.org/groups/virt/virtio-win/direct-
downloads/latest-virtio/virtio-win.iso -o /iso/virtio-win.iso  
  
# Add entrypoint script  
ADD entrypoint.py /entrypoint.py  
  
ENTRYPOINT ["/usr/bin/python3","-u","/entrypoint.py"]  

