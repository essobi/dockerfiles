# Tox network node  
FROM debian  
LABEL Description="This image is used to run Tox network node" Vendor="n/a"
Version="0.0.0"  
# Tox core code and nodes config download  
ADD https://github.com/irungentoo/toxcore/archive/master.zip
https://tox.0x10k.com/bootstrapd-conf-ipv64.txt /tmp/tox/  
# Updates, libs and build tools  
WORKDIR /tmp/tox  
RUN export BUILD_PACKAGES="automake \  
autotools-dev \  
build-essential \  
check \  
checkinstall \  
git \  
libtool \  
libsodium-dev \  
unzip \  
yasm" && \  
export RUNTIME_PACKAGES="libsodium18 \  
libconfig-dev" && \  
apt-get update && apt-get install -y $BUILD_PACKAGES $RUNTIME_PACKAGES && \  
unzip -tq master.zip && \  
unzip -aq master.zip && \  
cd toxcore-master && \  
./autogen.sh && \  
./configure --prefix=/usr --enable-daemon && \  
make && \  
# tests run  
# for i in $(seq 1 10); do echo "=== check attempt $i ==="; make check;
ret=$?; echo "=== check returned $ret ==="; if [ $ret -eq 0 ]; then echo "===
check passed ==="; break; elif [ $i -eq 10 ]; then echo "=== too many
failures, aborting ==="; exit 1; fi; done && \  
checkinstall --default \--pkgversion=0.0.0 && \  
echo "====== Installation completed ======" && \  
useradd --home-dir /var/lib/tox-bootstrapd \  
\--create-home --system \  
\--shell /usr/sbin/nologin \  
\--comment "TOX DHT bootstrap daemon" \  
\--user-group tox-bootstrapd && \  
chmod 700 /var/lib/tox-bootstrapd && \  
install -o tox-bootstrapd -g tox-bootstrapd -d /var/run/tox-bootstrapd && \  
install -m 755 -p other/bootstrap_daemon/tox-bootstrapd.sh /etc/init.d/tox-
bootstrapd && \  
sed -i 's|DAEMON=/usr/local/bin/$NAME|DAEMON=/usr/bin/$NAME|' /etc/init.d/tox-
bootstrapd && \  
update-rc.d tox-bootstrapd defaults && \  
install other/bootstrap_daemon/tox-bootstrapd.conf /etc/tox-bootstrapd.conf &&
\  
sed -i 's/enable_lan_discovery = true/enable_lan_discovery = false/' /etc/tox-
bootstrapd.conf && \  
sed -i 's/tcp_relay_ports = \\[443, 3389, 33445\\]/tcp_relay_ports = \\[8080,
33445\\]/' /etc/tox-bootstrapd.conf && \  
sed -i 's/motd = "tox-bootstrapd"/motd = "tox-bootstrapd docker"/' /etc/tox-
bootstrapd.conf && \  
sed -i '/^bootstrap_nodes = /,$d' /etc/tox-bootstrapd.conf && \  
cat /tmp/tox/bootstrapd-conf-ipv64.txt >> /etc/tox-bootstrapd.conf && \  
cd / && \  
apt-get remove --purge -y $BUILD_PACKAGES && \  
apt autoremove -y && \  
apt-get install -y $RUNTIME_PACKAGES && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
WORKDIR /  
  
# Ports  
EXPOSE 33445/tcp 33445/udp 8080/tcp 8080/udp  
  
# Run cmd  
#CMD ["/bin/bash"]  
USER tox-bootstrapd  
CMD ["/usr/bin/tox-bootstrapd", "--config=/etc/tox-bootstrapd.conf", "--
foreground", "--log-backend=stdout"]  

