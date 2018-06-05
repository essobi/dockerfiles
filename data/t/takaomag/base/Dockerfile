# takaomag/base  
  
FROM quay.io/takaomag/archlinux:2018.03.08.08.04  
  
MAINTAINER takaomag  
  
ENV \  
container=docker \  
X_DOCKER_ID=takaomag \  
X_DOCKER_REPO_NAME=base \  
X_PY3_VERSION=3.6.4 \  
# X_PY2_VERSION=2.7.14 \  
LANG=en_US.UTF-8 \  
X_J2TMPL_VERSION=0.0.3  
  
ADD files/tmp/install_python.sh /tmp/install_python.sh  
  
RUN \  
echo "2016-03-03-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
chown root:root /tmp/install_python.sh && \  
chmod 744 /tmp/install_python.sh && \  
: && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
# sudo -u nobody yaourt -Syy && \  
sudo -u x-aur-helper yay -Syy --noprogressbar && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}" &&
\  
pacman-key --refresh-keys && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Refreshed package developer
keys${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Update packages${FONT_DEFAULT}" && \  
cd /var/tmp && \  
# sudo -u nobody yaourt -Syua --noconfirm --noprogressbar && \  
sudo -u x-aur-helper yay -Syu --noconfirm --noprogressbar && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update packages${FONT_DEFAULT}" && \  
: && \  
REQUIRED_PACKAGES=("dhclient" "gperftools" "jemalloc" "libutil-linux" "pkg-
config" "iproute2" "nftables" "glib2" "autoconf" "automake" "make" "cmake"
"ccache" "libtool" "patch" "flex" "openssl" "zlib" "bzip2" "lzo" "lz4" "xz"
"unzip" "snappy" "protobuf" "blosc" "zeromq" "libuv" "libevent" "libev"
"libatomic_ops" "libaio" "sqlite" "mhash" "libsodium" "apr" "libnet" "curl"
"wget" "pcre" "bison" "expat" "libxml2" "libxslt" "libidn" "gettext" "ncurses"
"readline" "giflib" "libjpeg-turbo" "libpng" "btrfs-progs" "bcache-tools"
"fuse" "inotify-tools" "dstat" "strace" "sysdig" "htop" "iftop" "iotop"
"sysstat" "lsof" "tcpdump" "gnu-netcat" "socat" "openssh" "pssh" "bind-tools"
"ethtool" "ipcalc" "sipcalc" "ipv6calc" "rsync" "bash-completion" "jq"
"mercurial" "git" "subversion" "python" "python-pip" "python-setuptools"
"python-wheel" "cython" "ipython" "python-click" "python-systemd" "python-
pytz" "python-dateutil" "python-arrow" "python-requests" "python-boto3"
"python-pystache" "python-psutil" "python2" "python2-pip" "python2-setuptools"
"python2-wheel" "python2-virtualenv" "jdk9-openjdk" "jdk8-openjdk"
"jdk7-openjdk" "maven" "jna" "gdbm" "libffi" "gitflow-avh" "google-glog"
"porg" "aws-cli") && \  
# Removed packages  
# openvswitch  
# python-boto3 and aws-cli packages have a install problem because of strict
upper bound dependencies.  
# REQUIRED_PACKAGES+=("python-boto3" "aws-cli")  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
# sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
${REQUIRED_PACKAGES[@]} && \  
sudo -u x-aur-helper yay -S --needed --noconfirm --noprogressbar
${REQUIRED_PACKAGES[@]} && \  
mv /var/log/porg /var/db/. && \  
ln -sf /var/db/porg /var/log/porg && \  
sed --in-place -e "s/^#\\(LOGDIR=\/var\/log\/porg\\)$/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME} #\1\nLOGDIR=\/var\/db\/porg/g"
/etc/porgrc && \  
sed --in-place -e "s/^#\\(EXCLUDE=.\\+\\)/#
${X_DOCKER_ID}\/${X_DOCKER_REPO_NAME}
#\1\n\1:\/var\/tmp:\/usr\/src:\/usr\/local\/src:\/mnt\/ephemeral\/var\/tmp:\/mnt\/ebs.0\/var\/tmp:\/mnt\/local\/var\/tmp/g"
/etc/porgrc && \  
archlinux-java set java-9-openjdk && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install python-${X_PY3_VERSION}${FONT_DEFAULT}" &&
\  
/tmp/install_python.sh --python-version ${X_PY3_VERSION} \--prefix
/opt/local/python-${X_PY3_VERSION} \--base-working-dir /var/tmp && \  
cd /opt/local && \  
ln -sf python-${X_PY3_VERSION} python-$(echo ${X_PY3_VERSION} | cut -d '.' -f
1,2) && \  
ln -sf python-${X_PY3_VERSION} python-$(echo ${X_PY3_VERSION} | cut -d '.' -f
1) && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install
python-${X_PY3_VERSION}${FONT_DEFAULT}" && \  
: && \  
# echo -e "${FONT_INFO}[INFO] Install python-${X_PY2_VERSION}${FONT_DEFAULT}"
&& \  
# /tmp/install_python.sh --python-version ${X_PY2_VERSION} --prefix
/opt/local/python-${X_PY2_VERSION} --base-working-dir /var/tmp && \  
# cd /opt/local && \  
# ln -sf python-${X_PY2_VERSION} python-$(echo ${X_PY2_VERSION} | cut -d '.'
-f 1,2) && \  
# ln -sf python-${X_PY2_VERSION} python-$(echo ${X_PY2_VERSION} | cut -d '.'
-f 1) && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install
python-${X_PY2_VERSION}${FONT_DEFAULT}" && \  
#: && \  
echo -e "${FONT_INFO}[INFO] Installing Mustache Mo${FONT_DEFAULT}" && \  
curl --fail --silent --location --retry 5
"https://raw.githubusercontent.com/tests-always-included/mo/master/mo" -o
/opt/local/bin/mo && \  
chmod 755 /opt/local/bin/mo && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed Mustach Mo${FONT_DEFAULT}" && \  
: && \  
echo -e "${FONT_INFO}[INFO] Installing
j2tmpl-${X_J2TMPL_VERSION}${FONT_DEFAULT}" && \  
/opt/local/python-3/bin/pip3 install --upgrade
git+https://github.com/takaomag/j2tmpl@${X_J2TMPL_VERSION}#egg=j2tmpl && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Installed
j2tmpl-${X_J2TMPL_VERSION}${FONT_DEFAULT}" && \  
: && \  
rm -f /tmp/install_python.sh && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  

