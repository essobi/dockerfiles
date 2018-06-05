# PowerDNS-Admin  
# https://github.com/ngoduykhanh/PowerDNS-Admin  
FROM winggundamth/ubuntu-base:trusty  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=trusty-20160503.1  
# 1) Add user web to run PowerDNS-Admin  
# 2) Update and install python and required packages to compile library  
# 3) Install pip latest version  
# 4) Clone PowerDNS-Admin  
# 5) Install dependencies  
# 6) Clean to reduce Docker image size  
ENV APP_USER=web APP_NAME=powerdns-admin  
ENV APP_PATH=/home/$APP_USER/$APP_NAME  
ARG APT_CACHER_NG  
ARG DEVPI_SERVER  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
[ -n "$DEVPI_SERVER" ] && \  
mkdir -p ~/.pip && \  
echo "[global]\n\  
index-url = $DEVPI_SERVER\n\  
trusted-host = \  
$(echo $DEVPI_SERVER | awk -F/ '{print $3}' | awk -F: '{print $1}')\n\  
" >> ~/.pip/pip.conf || true; \  
useradd -s /bin/bash -d /home/$APP_USER -m $APP_USER && \  
apt-get update && \  
apt-get install -y curl git python libpython2.7 python-dev libsasl2-dev \  
build-essential libmariadbclient18 libmariadbclient-dev libssl-dev \  
libldap2-dev && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
sudo -u $APP_USER -H git clone \  
https://github.com/ngoduykhanh/PowerDNS-Admin.git \  
$APP_PATH && \  
pip install -r $APP_PATH/requirements.txt && \  
apt-get remove --purge --auto-remove -y \  
binutils build-essential cpp cpp-4.8 dpkg-dev fakeroot g++ g++-4.8 gcc \  
gcc-4.8 libalgorithm-diff-perl libalgorithm-diff-xs-perl libgcc-4.8-dev \  
libalgorithm-merge-perl libasan0 libatomic1 libc-dev-bin libc6-dev \  
libcloog-isl4 libdpkg-perl libfakeroot libfile-fcntllock-perl \  
libgmp10 libgomp1 libisl10 libitm1 libmpc3 libmpfr4 libquadmath0 \  
libstdc++-4.8-dev libtimedate-perl libtsan0 linux-libc-dev make manpages \  
manpages-dev patch xz-utils curl python-dev libmariadbclient-dev \  
libssl-dev libldap2-dev libsasl2-dev && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \  
/etc/apt/apt.conf.d/11proxy /root/.cache /root/.pip  
  
# 1) Copy Docker entrypoint script  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
USER $APP_USER  
WORKDIR $APP_PATH  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["python", "run.py"]  
EXPOSE 9393  
VOLUME ["/var/log"]  

