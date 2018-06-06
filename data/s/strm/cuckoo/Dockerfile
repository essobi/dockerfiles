FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
# Useful packages  
git curl wget vim \  
# Needed packages  
autoconf\  
automake\  
bridge-utils\  
build-essential\  
dh-autoreconf\  
libcap2-bin\  
libcurl4-gnutls-dev\  
libffi-dev\  
libfreetype6-dev\  
libfuzzy-dev\  
libjpeg62-turbo-dev\  
liblcms2-dev\  
libmagic-dev\  
libssl-dev\  
libtiff5-dev\  
libtool\  
libvirt-bin\  
libvirt-clients\  
libwebp-dev\  
libxml2-dev\  
libxmlsec1-dev\  
python\  
python-bottle\  
python-bson\  
python-chardet\  
python-dev\  
python-dpkt\  
python-gridfs\  
python-jinja2\  
python-libvirt\  
python-magic\  
python-pefile\  
python-pip\  
python-pil\  
python-pyrex\  
python-sqlalchemy\  
python-tk\  
qemu\  
qemu-kvm\  
qemu-system\  
qemu-system-arm\  
qemu-system-x86\  
tcl8.5-dev\  
tcpdump\  
tk8.5-dev\  
ubuntu-dev-tools\  
virtinst\  
zlib1g-dev\  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Permissions and security  
#RUN useradd --system --uid 666 -M --shell /usr/sbin/nologin cuckoo && \  
# chown cuckoo -R /code && \  
# usermod -a -G libvirtd cuckoo  
#USER cuckoo  
#RUN setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump  
# OR  
# RUN chmod +s /usr/sbin/tcpdump  
# Setup ssdeep & pydeep-master  
# Setup jansson.  
# Setup Yara  
# Setup Volatility  
# Setup Cuckoo  
RUN pip install sqlalchemy yara  
RUN pip install cybox==2.0.1.4  
RUN pip install maec==4.0.1.0  
RUN pip install python-dateutil  
RUN pip install pydeep  
RUN pip install scapy==2.3.2  
RUN pip install pycrypto  
RUN pip install cuckoo==2.0.1  
RUN pip install 'requests[security]==2.7.0'  
  
RUN cd /tmp && \  
wget --no-proxy https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
wget --no-proxy
http://downloads.volatilityfoundation.org/releases/2.4/volatility-2.4.zip && \  
unzip volatility-2.4.zip && \  
cd volatility-2.4 && \  
python setup.py install && \  
pip install distorm3  
  
# Copy default configuration files  
COPY conf /cuckoo  
  
# Setup virtualization  
COPY libvirt-conf /etc/libvirt  
  
WORKDIR /templates/  
# Install Windows Image  
ARG URL_WINDOWS81_QCOW  
ENV URL_WINDOWS81_QCOW ${URL_WINDOWS81_QCOW:-}  
RUN [ -z "$URL_WINDOWS81_QCOW" ] && exit 0 || wget --no-proxy
"$URL_WINDOWS81_QCOW"  
  
ARG URL_WINDOWS7_QCOW  
ENV URL_WINDOWS7_QCOW ${URL_WINDOWS7_QCOW:-}  
RUN [ -z "$URL_WINDOWS7_QCOW" ] && exit 0 || wget --no-proxy
"$URL_WINDOWS7_QCOW"  
  
#RUN service libvirtd start && \  
# virsh start CuckooSandbox && \  
# sleep 1200 && \  
# virsh snapshot-create-as --domain CuckooSandbox --name CuckooSandbox-Clean  
# Install Andoird Image  
# Install Linux Image  
VOLUME /vms  
  
EXPOSE 5900  
EXPOSE 8080  
VOLUME /data  
WORKDIR /data  
  
COPY main.sh /  
ENTRYPOINT ["/main.sh"]  
CMD ["default"]  

